# Import necessary modules
from fastapi import FastAPI, BackgroundTasks
from dotenv import load_dotenv
from bloom.text_generation import TextGenerator

# Create a FastAPI application instance
app = FastAPI()

# Define a function to write log messages to a file
def write_log(message: str):
    with open("log.txt", "a") as file:
        file.write(f"{message}\n")

# Define an example endpoint that adds a background task to write a log message
@app.get("/example")
async def example_endpoint(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Example endpoint was visited")
    return {"message": "This is an example endpoint"}

# Define an endpoint to generate text based on a user prompt
@app.get("/get_text")
async def get_text(background_tasks: BackgroundTasks, prompt: str):
    # Create an instance of the TextGenerator class
    text_generator = TextGenerator()
    
    # Generate text using the TextGenerator class based on the provided prompt
    text = text_generator.generate_text(prompt)
    
    # Add a background task to write a log message
    background_tasks.add_task(write_log, "Get text endpoint was visited")
    
    # Return the generated text as a response
    return {"text": text}


# Run the FastAPI application if this script is executed
if __name__ == "__main__":
    # Import the uvicorn server and run the FastAPI application
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
