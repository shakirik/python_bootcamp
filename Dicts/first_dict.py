cat = {
    "name": "tabby",
    "age": 21,
    "colour": "green"
}


# iteration 

for v in cat.values():
    print(v)

for k in cat.keys():
    print(k)

for k, v in cat.items():
    print(f"key is {k}, value is {v}")

# another way using dict keyword
cat2 = dict(name="cabby", age=10, colour="blue")
print(cat2)

# using in 

print("name" in cat)