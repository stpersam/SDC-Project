import requests
from time import sleep
from PIL import Image

#########################################
## make sure that the port of your app is set public
#########################################

url_user = "http://127.0.0.1:8000"
prompt = input("give me your prompt: ")

url = f"{url_user}/get_text?prompt={prompt}"
response = requests.post(url)
print(response.text)

