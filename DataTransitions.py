import json
file_path = 'animals.json'

def json_to_list():
    try:
        with open(file_path, 'r') as file:
            animals = json.load(file)
        return animals
    except:
         return []
    

def list_to_json():
    pass