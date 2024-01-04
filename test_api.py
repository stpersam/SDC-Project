import requests
import json

#########################################
## make sure that the port of your app is set public
#########################################

url_user = "https://didactic-trout-7r95vvq456j2p546-8000.app.github.dev" #url of forwarded port
prompt = input("give me your prompt: ")

url = f"{url_user}/get_text?prompt={prompt}"
response = requests.get(url)
print(json.loads(response.text)["text"])

