# n = input("Enter your code: ")
# teencode  = {
#     "code":"table",
#     "translation": "Cái bàn!"
# }
# if teencode["code"] == n:
#     print(teencode["code"],teencode["translation"] )
# else: 
#     print("Không có em ơi !")

teen_code_dict = {
    "eny":"Em người yêu!",
    "any":"Anh người yêu!",
    "nm":"Ngày mai!"
}
while True:
    code = input("Nhập vào Key muốn tìm kiếm: ")
    if code in teen_code_dict:
        print(teen_code_dict[code])
    else: 
        print("Không có key này trong danh sách!")
        choice = input("Bạn có muốn nhập vào dữ liệu này không ? (Y/N)")
        if choice == "y" or "Y":
            teen_code_dict_value = input("Nhập vào value: ")
            teen_code_dict[code] = teen_code_dict_value
        else:
            print("Xin cảm ơn !")