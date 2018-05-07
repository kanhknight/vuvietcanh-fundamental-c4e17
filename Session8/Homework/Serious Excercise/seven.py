def remove_dollar_sign(s):
    n = "This is Dollas strings: $ $ $ $ $ $"
    print(n)
    a= n.replace("$", "{0}".format(s))
    print(a)
in_put = input("Nhập vào chuỗi muốn thay thế: ")
remove_dollar_sign(in_put)