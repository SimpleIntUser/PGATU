list = [
    "apple",
    "banana",
    "cherry",
]
fruit = "cherry"
if fruit in list:
    print(f"Yes, {fruit} is in the list on index {list.index(fruit)}")
else:
    print(f"No, {fruit} is not in the list")