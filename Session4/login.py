from getpass import *
# Cách 1 sử dụng while và điều kiện
# n = 0
# while n<3:
#     n +=1
#     user = input("Username: ")
#     password = getpass("Password: ")
#     if user != "c4e":
#         print("No Such User")
#         mess = ("Bạn còn {0} lần nhập nữa!".format(3-n))
#         print(mess)
#     else:
#         if password != "codethechange":
#             print("Password Wrong!")
#             mess = ("Bạn còn {0} lần nhập nữa!".format(3-n))
#             print(mess)
#         else:
#             print("Welcome",user)

# Thoát khỏi vòng lặp break -> Break sẽ tìm vòng lặp gần nhất để thoát ra

# Cách 2 sử dụng while và break
n = 0
while True:
    n+=1
    user = input("Username: ")
    password = getpass("Password: ")
    if user != "c4e":
        print("No Such User")
        mess = ("Bạn còn {0} lần nhập nữa!".format(3-n))
        print(mess)
        if (3-n)==0:
            break
    else:
        if password != "codethechange":
            print("Password Wrong!")
            mess = ("Bạn còn {0} lần nhập nữa!".format(3-n))
            print(mess)
            if (3-n)==0:
                break
        else:
            print("Welcome",user)
            break