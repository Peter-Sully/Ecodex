import requests # type: ignore
import json

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

