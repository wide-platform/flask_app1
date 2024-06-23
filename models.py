import json

def json_load():
    with open ("q&a.json", "r") as read:   
        return json.load(read)
    
def save_db():
    with open ("q&a.json", "w") as write:
        return json.dump(db,write)    

db=json_load()