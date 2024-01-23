# Import necessary modules
from fastapi import FastAPI, BackgroundTasks
from dotenv import load_dotenv
from bloom.text_generation import TextGenerator

import datetime
import time
from wandb.sdk.data_types.trace_tree import Trace
import os
import wandb

# Create a FastAPI application instance
app = FastAPI()

os.environ['WANDB_NOTEBOOK_NAME'] ='test_model.ipynb'

os.environ['WANDB_API_KEY'] = 'fb7fc2fa1c4815db6b7169837af61bf3bd7edd10'

wandb.login()
wandb.init(project="sdc-project")

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
    start_time = round(datetime.datetime.now().timestamp() * 1000)
    # Create an instance of the TextGenerator class
    text_generator = TextGenerator()
    
    # Generate text using the TextGenerator class based on the provided prompt
    text = text_generator.generate_text(prompt)
    
    # Add a background task to write a log message
    background_tasks.add_task(write_log, "Get text endpoint was visited")
    llm_end_time_ms = round(datetime.datetime.now().timestamp() * 1000)

    log_to_wandb(start_time, llm_end_time_ms, prompt,text)

    # Return the generated text as a response
    return {"text": text}


def log_to_wandb(start_time_ms, end_time_ms, prompt, response):
    root_span = Trace(
        name="root_span",
        kind="llm",  # kind can be "llm", "chain", "agent" or "tool"
        status_code='SUCCESS',
        status_message='ok',
        metadata={
            "model_name": 'bloom-560m',
            "duration": str(end_time_ms - start_time_ms)
        },
        start_time_ms=start_time_ms,
        end_time_ms=end_time_ms,
        inputs={"system_prompt": 'system_message', "query": prompt},
        outputs={"response": response},
    )
    root_span.log(name="bloom_tracer")


# Run the FastAPI application if this script is executed
if __name__ == "__main__":
    # Import the uvicorn server and run the FastAPI application
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
