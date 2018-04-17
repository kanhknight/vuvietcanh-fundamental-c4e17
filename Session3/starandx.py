m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))
for i in range(m):
    for j in range(n):
        if (i+j)%2!=0:
            print("* ",end ="")
        else:
            print("o ", end ="")
    print()