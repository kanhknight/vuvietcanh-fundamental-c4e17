n = int(input("Enter Number: "))
count = 1.00
if n>=1:
    for i in range(n):
        if i !=0:
            count = count+(1/(i+1))
print(count)