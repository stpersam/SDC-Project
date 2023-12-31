from fastapi import FastAPI, BackgroundTasks
from dotenv import load_dotenv
from bloom.text_generation import TextGenerator


app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as file:
        file.write(f"{message}\n")

@app.get("/example")
async def example_endpoint(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Example endpoint was visited")
    return {"message": "This is an example endpoint"}

@app.get("/get_text")
async def get_text(background_tasks: BackgroundTasks,prompt: str):
    text_generator = TextGenerator()
    text = text_generator.generate_text(prompt)
    background_tasks.add_task(write_log, "Get text endpoint was visited")
    return {"text": text}

# OPTIONAL: Implement any necessary profanity checking or validation for the user prompts

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)