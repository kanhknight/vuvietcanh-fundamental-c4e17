# pythonic
nums = [1,-2,3,83,4,33,-60,-88]

x = int(input("Enter a interger: "))

# Cách kiểm tra 1 phần tử có trong list hay không
# in
# Sử dụng in có cơ hội được dừng lại trước - xài cái này tốt hơn
if x in nums:
    print("Found in list")
else:
    print("Not found in list")

# Muốn đếm số phần tử
# occurences => count()
c = nums.count(x)
print(c)