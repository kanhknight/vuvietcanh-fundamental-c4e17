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
# n = 0
# while True:
#     n+=1
#     user = input("Username: ")
#     password = getpass("Password: ")
#     if user != "c4e":
#         print("No Such User")
#         mess = ("Bạn còn {0} lần nhập nữa!".format(3-n))
#         print(mess)
#         if (3-n)==0:
#             break
#     else:
#         if password != "codethechange":
#             print("Password Wrong!")
#             mess = ("Bạn còn {0} lần nhập nữa!".format(3-n))
#             print(mess)
#             if (3-n)==0:
#                 break
#         else:
#             print("Welcome",user)
#             break

# Cách 3 sử dụng biến chứa True và False
# n = True
# while True:
#     user = input("Username: ")
#     password = getpass("Password: ")
#     if user != "c4e":
#         print("No Such User")
#     else:
#         if password != "codethechange":
#             print("Password Wrong!")
#             n = False
#         else:
#             print("Welcome",user)
#             n = False

# Cách 4 sử dụng điều kiện trong if và biến chứa True và False
n = True
m = 0
while True:
    m +=1
    user = input("Username: ")
    password = getpass("Password: ")
    if user != "c4e":
        print("No Such User")
        if (3-m)==0:
            n = False
    else:
        if password != "codethechange":
            print("Password Wrong!")
            if (3-m)==0:
                n = False
        else:
            print("Welcome",user)
            n = False