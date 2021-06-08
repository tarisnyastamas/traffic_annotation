import json

def load_json(filename: str):
    with open(filename, encoding='UTF-8') as f:
        return json.load(f)