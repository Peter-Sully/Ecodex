import requests # type: ignore
import json
from pprint import pprint

def scientificNameFromImage(image_path : str) -> str:
    API_KEY = "2b10uneIXKpVTSEFhRzryEJ6W"  # our API key
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

    with open(image_path, 'rb') as image_data:
        files = [('images', (image_path, image_data))]

        req = requests.post(api_endpoint, files=files)

        json_result = json.loads(req.text)

        pprint(req.status_code)
        pprint(json_result)


scientificNameFromImage("./data/image_1.jpeg")

api_url = f"https://explorer.natureserve.org/api/data/"
payload = {
    "criteriaType": "species",
    "textCriteria": [{
        "paramType": "textSearch",
        "searchToken": "epilobium canum",
        "matchAgainst": "allNames",
        "operator": "similarTo"
    }],
    "statusCriteria": [],
    "locationCriteria": [],
    "pagingOptions": {
        "page": None,
        "recordsPerPage": None
    },
    "recordSubtypeCriteria": [],
    "modifiedSince": None,
    "locationOptions": None,
    "classificationOptions": None,
    "speciesTaxonomyCriteria": []
}
# print(payload)
response = requests.post(api_url+"speciesSearch", json=payload)
uniqueId = response.json()["results"][0]["uniqueId"]
# print(response.status_code)
# print(response.json())
print(uniqueId)

response = requests.post(api_url+"taxon/"+uniqueId)

print(response.json())