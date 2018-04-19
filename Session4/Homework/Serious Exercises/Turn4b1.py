value0 = 0
value1 = 1
value_list = []
n = int(input("Enter a number: "))
for i in range (n):
    if i%2 == 0:
        value_list.append(value1)
    else:
        value_list.append(value0)
print(*value_list)