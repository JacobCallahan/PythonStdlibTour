"""Python's JSON module is a must for most of us"""
import json

data = {"location": "Raleigh", "temperalure": 70, "humidity": 50}

with open("export.json", "w") as ex_file:
    json.dump(data, ex_file, indent=4, sort_keys=True)

data_str = json.dumps(data, indent=4)
print(data_str)


with open("export.json") as im_file:
    loaded_data = json.load(im_file)

loaded_str = json.loads(data_str)
