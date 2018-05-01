nums = [22,-65,984,33,22,4,-894]
x = int(input("Enter an integer: "))

# Không sử dụng count(), in hoặc int()
# Tìm từ đầu đến cuối : Linear Search =>> BigO =>> O(n) =>> Worstcase !
# for num in nums:
#     if num == x:
#         print("Found!")
#         break
# else:
#         print("Not Found")

# found  = False
# for num in nums:
#     if num == x:
#         found = True
#         break

# if found:
#     print("Found!")
# else: 
#     print("Not Found!")

for num in nums:
    if num ==x:
        print("Found!")
        break