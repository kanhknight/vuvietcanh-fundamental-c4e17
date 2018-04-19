value0 = 0
value1 = 1
value_list = []
for i in range (6):
    if i%2 == 0:
        value_list.append(value1)
    else:
        value_list.append(value0)
print(*value_list)