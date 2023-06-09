import json


def load_json_config(path_to_file="midjourney_config.json"):
    with open(path_to_file, "r") as json_file:
        params = json.load(json_file)

    return params
