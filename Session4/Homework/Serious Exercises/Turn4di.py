n = int(input("Enter a number: "))
for j in range(n):
    for i in range(n):
        if (i+j) % 2 == 0:
            print(1, end = " ")
        else:
            print(0, end =" ")
    print()