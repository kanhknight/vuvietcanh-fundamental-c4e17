favor = ["Kẹo", "Bánh", "Phim"]
n = input("Add new item: ")
favor.append(n)
print(*favor,sep=", ") #Cái này là thay cho lệnh duyệt mảng
for i in range(len(favor)):
    print(favor[i],end = " ")
print()