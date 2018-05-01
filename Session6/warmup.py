n_lits  = [15,2,3,4,535,6,7,8,9,0]
x = int(input("Nhập Vào 1 số nguyên: "))
for n in n_lits:
    if x == n:
        print("Chuỗi có chứa phần tử {0} bạn vừa nhập".format(n))
        break
else:
        print("Chuỗi không có chứa phần tử bạn vừa nhập")

# for i in range(len(n_lits)):
#     if (i+1) == x:
#         print(n_lits[i])