# Cách 1:
# n = int(input("Enter a number: "))
# for j in range(n):
#     for i in range(n):
#         if (i+j) % 2 == 0:
#             print(1, end = " ")
#         else:
#             print(0, end =" ")
#     print()

# Cách 2:
n = int(input("Enter a number: "))
for j in range(n):
    n_list = []
    for i in range(n):
        n_list.append(i)
        for k in range(len(n_list)):
            if (k*j)%2 == 0:
                n_list[k] = 1
            else:
                n_list[k] = 0
    print(*n_list)
print()