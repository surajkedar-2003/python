import json
from pathlib import Path

user = {
    "name": "Suraj",
    "age": 25,
    "skills": ["Python", "Java"]
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)  # This line serializes the user dictionary into JSON format and writes it to the "user.json" file with an indentation of 4 spaces for better readability.



#read the json file
file_path = Path("files") / "config.json"
with open(file_path, "r") as file:
    config = json.load(file)  # This line deserializes the JSON content from the "config.json" file and loads it into the config variable as a Python dictionary.
    print(config)  # This line prints the contents of the config dictionary to the console.

admin = config["admin"]  # This line accesses the value associated with the "admin" key in the config dictionary and assigns it to the admin variable.
print(admin)  # This line prints the value of the admin variable to the console.

json_string = json.dumps(user)
print(json_string)
print(type(json_string))


data = json.loads(json_string)
print(data)