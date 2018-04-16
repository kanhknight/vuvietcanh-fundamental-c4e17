while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    items = ["T-shirt", "Sweater"]
    if n == "R":
        print("Our items: ", end = "")
        print(*items, sep = ", ")
    if n == "C":
        item = input("Enter new item: ")
        items.append(item)
        print("Our items: ", end = "")
        print(*items, sep = ", ")
    if n == "U":
        items = ["T-shirt", "Sweater", "Jeans"]
        position = int(input("Update Position: "))
        position = position -1
        update_item = input("New item? ")
        items[position] = update_item
        print("Our items: ", end = "")
        print(*items, sep = ", ")
    if n == "D":
        items = ["T-shirt", "Sweater", "Jeans"]
        position = int(input("Delete Position: "))
        position = position -1
        # del items[position];
        itemx = items[position]
        items.remove(itemx)
        print("Our items: ", end = "")
        print(*items, sep = ", ")