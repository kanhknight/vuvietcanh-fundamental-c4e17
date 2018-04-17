# names = []
# print(names, type(names))
names = ["Canh", "Hieu", "Duc Anh", "Don"]
# Create
# names.append("Hong")
# a = "Hoai"
# names.append(a)
# print(names)

# Read
# print(names[0]) #in một phần tử
# print(*names) #in cả list
# print(*names, sep =", ") #in cả list và có chia tách
# Truy cập phần tử trong list như 1 biến và làm việc như 1 biến bình thường
# List cuốn được 1 vòng, cuốn -n+1 sẽ báo lỗi

# Get length of list (len(names))
# Update 
# names[0] = "Vu Viet Canh"
# print(*names, sep=", ")

# len(names)

# for i in range(len(names)):
#     print(i+1,". ",names[i])

# foreach
# for n in names:
#     print(names.index(n)+1, ". ", n)

# foreach
index = 1
for n in names:
    # print(index,". ",n,sep="") # Ngăn điều khiển khoảng cách của chuỗi thay vì mặc định của python
    # string format
    message = "{0}. {1}".format(index, n)
    index = index+1 #no +=1
    print(message)

#remove : listname.remove()