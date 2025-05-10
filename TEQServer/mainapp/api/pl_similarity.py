import requests

from mainapp.api.gateway import GATEWAY

URL = f"{GATEWAY}/pl/similarity/"

def calculate_similarity(code1, code2):
    response = requests.post(URL, json={"code1": code1, "code2": code2})

    if response.ok:
        data = response.json()
        if "similarity" not in data:
            raise Exception("No similarity found")
        return data["similarity"]

    raise Exception(f"{response.status_code} - {response.text}")