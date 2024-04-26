friends_ages = {"Rolf" : 24, "Jhon" : 30, "Adam": 27}

#print(friends_ages["Adam"])

for student, age in friends_ages.items():
    print(f"{student}: {age}")

friends = [
    {"name":"Rolf", "age" : 24},
    {"name":"Adam", "age" : 30},
    {"name":"Adam", "age" : 27},
]

#print(friends[0]["name"])