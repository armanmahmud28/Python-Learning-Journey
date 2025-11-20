import json
x = '{"name":"Nahid", "age": 21, "city":"Dhaka"}'
y = json.loads(x)

print(y)


# Dictionary List
a = {
    "name": "arman",
    "age": 22,
    "city": "Dhaka"
}

b = json.dumps(a)
print(b)
