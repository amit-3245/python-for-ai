info = {
    "name": "amit",
    "cgpa": 9.5,
    "subjects": ["python", "java", "c++"],
    3.14: "pi"
}
print(type(info))
print(info)
info["cgpa"] = 9.6
print(info[3.14])

#methods
"""
d.keys()
d.values() returns all keys and values
d.items()  returns key value pairs
d.get(val)
d.update(new_item)

"""

dict_keys = info.keys()
print(type(dict_keys))

dict_vals = list(info.values())
print(dict_vals)

print(info.items())

print(info.get("cgpa"))
print("end of code ")


info.update(
    {
        "city": "Dehli"
    }
)
