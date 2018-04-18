# Write a program to count number occurrences in a list, with OR without using count() function
numbers = [1,6,8,1,2,1,5,6]
n = int(input("Enter a number? "))
count = 0
for item in numbers:
    message = "{0}".format(item)
    if item ==n:
        count +=1
print("{0} appears {1} times in my list!".format(n,count))
print(count)