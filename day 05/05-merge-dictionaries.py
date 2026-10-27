"""
Merge two dictionaries. If a key exists in both, add their values together.

Example input:
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}



Expected output:
{"a": 10, "b": 50, "c": 40}
"""
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40, "d": 50}

result = dict1.copy()

for key in dict2:
    if key in result:
        result[key] += dict2[key]
    else:
        result[key] = dict2[key]

print(result)
