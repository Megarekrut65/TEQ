import requests

from mainapp.api.gateway import GATEWAY

URL = f"{GATEWAY}/nl/similarity/"

def calculate_similarity(text1, text2):
    response = requests.post(URL, json={"text1": text1, "text2": text2})

    if response.ok:
        data = response.json()
        if "similarity" not in data:
            raise Exception("No similarity found")
        return data["similarity"]

    raise Exception(f"{response.status_code} - {response.text}")