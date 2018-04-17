items = ["T-shirt", "Sweater", "Jeans"]
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if n == "R":
        print("Our items: ", end = "")
        print(*items, sep = ", ")
    elif n == "C":
        item = input("Enter new item: ")
        items.append(item)
        print("Our items: ", end = "")
        print(*items, sep = ", ")
    elif n == "U":
        position = int(input("Update Position: "))
        position = position -1
        update_item = input("New item? ")
        items[position] = update_item
        print("Our items: ", end = "")
        print(*items, sep = ", ")
    elif n == "D":
        position = int(input("Delete Position: "))
        position = position -1
        # del items[position];
        itemx = items[position]
        items.remove(itemx)
        print("Our items: ", end = "")
        print(*items, sep = ", ")