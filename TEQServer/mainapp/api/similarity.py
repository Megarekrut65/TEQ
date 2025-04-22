import requests

URL = "http://127.0.0.1:8005/api"

def calculate_similarity(text1, text2):
    response = requests.post(f"{URL}/similarity/", json={"text1": text1, "text2": text2})

    if response.ok:
        data = response.json()
        if "similarity" not in data:
            raise Exception("No similarity found")
        return data["similarity"]

    raise Exception(f"{response.status_code} - {response.text}")