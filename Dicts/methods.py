# clear, copy, fromkeys, get, pop, popitem (remove random) and update 

cat = {
    "name": "tabby",
    "age": 21,
    "colour": "green"
}

# clear
cat.clear()
print(cat)

cat2 = {
    "name": "tabby",
    "age": 21,
    "colour": "green"
}

# copy
cat3 = cat2.copy()
print(cat2 == cat3)
print(cat2 is cat3)

# fromkeys - pass in iterable key/collection then assign a value

new_user = {}.fromkeys(["name", "age", "score", "email", "profile"], "none")
print(new_user)


# get

print(cat2.get('age'))
print(cat2.get('name'))

# pop - remove item from dict (have to provide key)

# popitem - removes a random item from the dictionary

# update - updates based on what you give, will overwrite same keys 

