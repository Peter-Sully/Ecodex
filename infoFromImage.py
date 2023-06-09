import requests  # type: ignore
import json
from pprint import pprint


def sciNameFromImage(image_data) -> str:
    API_KEY = "2b10uneIXKpVTSEFhRzryEJ6W"  # our API key
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"
    files = [("images", ("image_path", image_data))]
    req = requests.post(api_endpoint, files=files)
    json_result = json.loads(req.text)

    if req.status_code != 200:
        print("bad things happened, image recog API not 200 status code")
    try:
        return json_result["results"][0]["species"]["scientificNameWithoutAuthor"]
    except:
        print("failed to read pl@ntnet API json")
        print(json_result)
        return "404"


def infoFromsciName(sciName: str):
    api_url = f"https://explorer.natureserve.org/api/data/"
    payload = {
        "criteriaType": "species",
        "textCriteria": [
            {
                "paramType": "textSearch",
                "searchToken": sciName,
                "matchAgainst": "allNames",
                "operator": "similarTo",
            }
        ],
        "statusCriteria": [],
        "locationCriteria": [],
        "pagingOptions": {"page": None, "recordsPerPage": None},
        "recordSubtypeCriteria": [],
        "modifiedSince": None,
        "locationOptions": None,
        "classificationOptions": None,
        "speciesTaxonomyCriteria": [],
    }
    response = requests.post(api_url + "speciesSearch", json=payload)
    try:
        uniqueId = response.json()["results"][0]["uniqueId"]
    except:
        print(response)
        raise Exception("failed to read natureServe API Json")
    response = requests.post(api_url + "taxon/" + uniqueId)

    return response.json()


def infoFromImage(image_data):
    sciName = sciNameFromImage(image_data)  # accesses Pl@ntNet API to recognize image
    infoJson = infoFromsciName(
        sciName
    )  # accesses NatureServe Explorer REST API to get information about plant
    return infoJson


# sciName = sciNameFromImage("./data/image_1.jpeg")
# sciName = "Epilobium canum"
# plantdata = infoFromsciName(sciName)
# print("plant data:",plantdata)

# with open("./data/image_1.jpeg", "rb") as image_data:
#     theData = infoFromImage(image_data)
