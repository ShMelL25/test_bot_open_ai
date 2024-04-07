import json

def read(path_file:str):
    with open(path_file, encoding="utf-8") as f:
        templates = json.load(f)
    return templates
    
def write(path_file:str, json_file):
        
    with open(path_file, 'w', encoding="utf-8") as file:
        json.dump(json_file, file)