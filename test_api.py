import requests
from time import sleep
from PIL import Image

#########################################
## make sure that the port of your app is set public
#########################################

url_user = "https://gc57pv84-8000.euw.devtunnels.ms"
prompt = input("give me your prompt: ")

url = f"{url_user}/get_text?prompt={prompt}"
response = requests.get(url)
print(response)

