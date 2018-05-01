person = {
    "name":"Quân",
    "age":22,
    "gender": "undefined",
    "address": "Ha Noi",
    "login_count":8
}

# if "name" in person: # Tương đương in person.keys()
#     print("Yeahhhh!")

print(person.keys())
print(person.values())

if "Quân" in person.values():
    print("Có nhé")