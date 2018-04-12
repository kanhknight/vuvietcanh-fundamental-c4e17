n = int(input("Enter Your Total: "))
for i in range(n):
    if i % 2:
        print("X ", end = "")
    else:
        print("* ", end = "")
print("\n")