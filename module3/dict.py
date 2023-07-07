user1 = {
    "name": "Sasha",
    "age": 22
}

user2 = {
    "name": "Eugene",
    "age": 28
}

print(user1['name'])
print(user2["name"])

count_dict = {
    345: 3,
    25: 2,
    10000: 5
}

print(count_dict)

print("name" in user1)
print("name_full" in user1)
print(user1.get("full_name"))
print(user1.get("full_name", "no name"))

print(len(user1))

print(list(user1.keys()))
print(list(user1.values()))
print(list(user1.items()))
