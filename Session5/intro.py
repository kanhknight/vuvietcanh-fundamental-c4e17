# Data Descriptive
# person = ["Quân", 40, "Single", "Hanoi", 2,11]
# Dictionary: key (Tên key bao giờ cũng ở dạng string) : value
# Khai báo 
# 
# Cách 1
# person = {}

# Cách 2
    # person  = {
    #     "name": "Cảnh"

    # }


#  Cách 3
person = {
    "name":"Cảnh",
    "age":"31",
    "home":"Yên Bái"
}

# if "home" in person: #list, str
#     print(person["home"])
# else:
#     print("Không có home trong chương trình!")

# person["age"] = 22 # Gán dữ liệu như 1 biến bình thường khi đã truy cập vào data.
# print(person["name"], person["age"])


# # Update Key
# person["age"] = 25

# # Create 
# person["job"] = "IT"

# #  Delete
# del person["name"]

# print(*person.keys())

# print(*person.values())

# for value in person.values():
#     print(value, end = " ")
# print()

for key,value in person.items():
    print("{0}: {1}".format(key,value))
print()
# print(person)
