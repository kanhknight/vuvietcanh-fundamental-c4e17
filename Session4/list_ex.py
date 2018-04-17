menu = ['Pho', 'Cơm Rang', 'Mì Xào', 3]
print(menu)
# Create

menu.append('Vịt Quay')
print("After append()")
print(menu)

# print(menu[-5]) # List chạy quay vòng được 1 vòng

# for i
# for i in range(len(menu)):
#     print(menu[i], end = " ")
# print()

# for each
# for m in menu: #item kiểu dữ liệu gì thì m trả về nguyên bản kiểu dữ liệu như vậy
#     print(m)

# for enum
for i, item in enumerate(menu):
    message = "{0}. {1}".format(i,item)
    print(message)

# String Format
name = "Cảnh Vũ"
age = 31
status = "Đã kết hôn"
address = "Hà Nội"
tin_nhan = ("Họ và tên: {0}\nTuổi: {1} \nTình trạng: {2} \nĐịa chỉ: {3}").format(name,age,status,address) # Hỏi Lại Về Việc Dùng Cái Này Ở Chỗ Khác Sau Khi Khai Báo
print(tin_nhan)