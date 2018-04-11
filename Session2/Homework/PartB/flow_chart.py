import webbrowser
# Định nghĩa 1 hàm
def say_hello(str):
    "Đây là function sẽ in ra 1 chuỗi chào mừng"
    print(str)
    return;

name = input("Nhập vào tên một người bạn: ")
if name == "Quan":
    print("Hand some")
elif name == "Tung":
    even_more_handsome = True
    print(bool(even_more_handsome))
elif name == "Don":
    say_hello(name)
else:
    webbrowser.open("https://www.youtube.com/watch?v=04854XqcfCY")
# Lưu đồ nằm ở link này : https://realtimeboard.com/app/board/o9J_kz3CoKA=/