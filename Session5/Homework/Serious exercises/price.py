prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}

total = 0
for key_price, value_price in prices.items():
    for key_stock, value_stock in stock.items():
        if key_price == key_stock:
            print(key_price)
            print("Price: {0}".format(value_price))
            print("Stock: {0}".format(value_stock))
            total_item = value_price * value_stock
            print("Total Money: {0}".format(total_item))
            print()
for num in prices and stock:
    total = total + (prices[num] * stock[num])
print(total)



