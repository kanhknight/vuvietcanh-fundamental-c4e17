# IN RA TAM GIAC CAN
# CACH 1
# n = int(input("Nhập vào số hàng: "))
# for i in range(0,n):
#     print("* " * (i+1))

# CACH 2
n = int(input("Nhập vào 1 số: "))
for i in range(n):
    for j in range(n):
        if j <=i:
            print("* ", end = "")
        else:
            print("  ",end = "")
    print()