import requests

from mainapp.api.gateway import GATEWAY


def run_code_tests(language, function_structure, function_type, unittests, script):
    url = f"{GATEWAY}/{language}/test/"

    response = requests.post(url, json={
        "functionStructure": function_structure,
        "functionType": function_type,
        "unittests": unittests,
        "script": script})

    if response.ok:
        data = response.json()
        if "detail" in data:
            raise Exception(data["detail"])
        return data

    raise Exception(f"{response.status_code} - {response.text}")