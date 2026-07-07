# methods
"""
json.loads() : it convert json string into python object
json.dumps() : it convert python object into json string


json.load() : it use for read json data 
json.dump() : it use for write json data


"""

import json


# ============================================================
# 1. json.loads()
# Converts JSON string into Python object
# JSON String  --->  Python Object
# ============================================================

json_str = '{"name": "Amit", "age": 21, "isStudent": true}'

# Convert JSON string into Python dictionary
python_obj = json.loads(json_str)

print("1. json.loads() Example")
print("Python Object:", python_obj)
print("Type:", type(python_obj))


print("\n" + "=" * 50)


# ============================================================
# 2. json.dumps()
# Converts Python object into JSON string
# Python Object  --->  JSON String
# ============================================================

student = {
    "name": "Amit",
    "age": 21,
    "isStudent": True
}

# Convert Python dictionary into JSON string
json_string = json.dumps(student)

print("2. json.dumps() Example")
print("JSON String:", json_string)
print("Type:", type(json_string))


print("\n" + "=" * 50)


# ============================================================
# 3. json.dump()
# Writes Python object into a JSON file
# Python Object  --->  JSON File
# ============================================================

student_data = {
    "name": "Amit",
    "course": "B.Tech CSE",
    "specialization": "AI Engineering"
}

# Open data.json file in write mode
# If file does not exist, Python will create it automatically
with open("data.json", "w") as file:

    # Write Python dictionary into JSON file
    json.dump(student_data, file, indent=4)

print("3. json.dump() Example")
print("Data successfully written to data.json")


print("\n" + "=" * 50)


# ============================================================
# 4. json.load()
# Reads JSON data from a JSON file
# JSON File  --->  Python Object
# ============================================================

# Open data.json file in read mode
with open("data.json", "r") as file:

    # Read JSON file and convert it into Python object
    loaded_data = json.load(file)

print("4. json.load() Example")
print("Loaded Data:", loaded_data)
print("Type:", type(loaded_data))