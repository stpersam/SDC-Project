import requests
import json

# Set the URL for the FastAPI application with the forwarded port
url_user = "https://didactic-trout-7r95vvq456j2p546-8000.app.github.dev"

# Prompt the user to input a prompt
prompt = input("give me your prompt: ")

# Construct the URL for the "/get_text" endpoint with the provided prompt
url = f"{url_user}/get_text?prompt={prompt}"

# Make an HTTP GET request to the FastAPI application
response = requests.get(url)

# Parse the response JSON and print the generated text
print(json.loads(response.text)["text"])
