n = int(input("Nhập vào số hàng: "))
m = int(input("Nhập vào số cột: "))
for i in range(n+1):
    for j in range(m+1):
        if j <=(m-i):
            print("  ",end = "")
        else:
            print("* ", end = "")
    print()