from getpass import *
while True:
    user = input("Username: ")
    password = getpass("Password: ")
    if user != "c4e":
        print("No Such User")
    else:
        if password != "codethechange":
            print("Password Wrong!")
        else:
            print("Welcome",user)
            break