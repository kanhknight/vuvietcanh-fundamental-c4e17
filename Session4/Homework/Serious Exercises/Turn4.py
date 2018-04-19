# Khai báo số phần tử có trong list
n = 20
# Khai báo list muốn làm việc
n_list = []
#Đưa phần tử thứ i vào list
for i in range(20):
    n_list.append(i)
# 0 numbers, starting from 0
print(*n_list,end = " ")
print()
# Ask users to enter a number, then print n positive numbers from 0 to n-1
lap = True
while lap:
    rm = int(input("Enter a number: "))
    for x in n_list:
        if rm == x:
            n_list.remove(x)
            print(*n_list,end = " ")
    print()