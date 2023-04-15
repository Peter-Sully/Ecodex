import requests

def get_plant_description(scientific_name):
    """Fetches plant description from NatureServe Explorer API using scientific name"""
    # NatureServe Explorer API endpoint for species search
    endpoint = "https://explorer.natureserve.org/api/data/speciesSearch"
    payload = {
        "text": scientific_name,
        "lang": "en",
        "per_page": 1,
        "page": 1
    }
    try:
        response = requests.get(endpoint, params=payload)
        response.raise_for_status() # Raise exception if response is not successful
        plant_data = response.json()
        # Extracting plant description from API response
        description = plant_data.get('results', [{}])[0].get('description', '')
        return description
    except requests.exceptions.HTTPError as e:
        print("Error fetching plant description from NatureServe Explorer API: ", e)
        return None
    except Exception as e:
        print("Error: ", e)
        return None

# Usage example
scientific_name = "Quercus alba" # Replace with the scientific name of the plant
description = get_plant_description(scientific_name)
if description:
    print("Plant description:")
    print(description)
else:
    print("Plant description not found.")
