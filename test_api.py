import requests
import json

# Prompt the user to input a url examp. https://didactic-trout-7r95vvq456j2p546-8000.app.github.dev
url_user = input("give me your url: ")

# Prompt the user to input a prompt
prompt = input("give me your prompt: ")

# Construct the URL for the "/get_text" endpoint with the provided prompt
url = f"{url_user}/get_text?prompt={prompt}"

# Make an HTTP GET request to the FastAPI application
response = requests.get(url)

# Parse the response JSON and print the generated text
print(json.loads(response.text)["text"])
