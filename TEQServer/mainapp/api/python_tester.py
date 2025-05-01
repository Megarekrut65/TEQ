import requests

URL = "http://127.0.0.1:8016/python/test/"

def python_run_tests(function_structure, function_type, unittests, script):
    response = requests.post(URL, json={
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