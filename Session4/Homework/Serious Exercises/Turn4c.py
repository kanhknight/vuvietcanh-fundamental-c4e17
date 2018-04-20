n_list=[]
n = int(input("Enter a number: "))
for i in range(n):
    n_list.append(i+1)

for i in range(len(n_list)):
    if i == 0:
        print(*n_list)
    else:
        j_list = []
        for j in n_list:
            j = n_list[0] * (i+1)
            j_list.append(j)
        print(*j_list)
    