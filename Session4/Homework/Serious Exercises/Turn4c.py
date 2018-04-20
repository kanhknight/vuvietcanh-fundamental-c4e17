# for i in range(1,10):
#     for j in range(1,10):
#         print (i*j, end = " ")
#     print()
n = int(input("Enter a number: \n"))
n_list = []
for j in range(n):
    n_list = []
    for i in range(n):
        n_list.append(i+1)
    for k in range(len(n_list)):
        n_list[k] = n_list[k]* (j+1)
    for m in n_list:
        if m < 10:
            print(m,end = "   ")
        elif m >=10:
            print(m,end = "  ")
    print()
print()