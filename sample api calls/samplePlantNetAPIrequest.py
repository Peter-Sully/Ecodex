import requests
import json
from pprint import pprint

API_KEY = "2b10uneIXKpVTSEFhRzryEJ6W"  # Set you API_KEY here
PROJECT = "all" # try "weurope" or "canada"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

image_path = "./data/image_1.jpeg"
image_data = open(image_path, 'rb')


files = [
    ('images', (image_path, image_data))
]

req = requests.post(api_endpoint, files=files)

json_result = json.loads(req.text)

pprint(req.status_code)
pprint(json_result)

image_data.close()

