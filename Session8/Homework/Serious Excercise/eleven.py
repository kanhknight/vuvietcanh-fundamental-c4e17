def is_inside(a,b):
    range1 = b[0] + b[2]
    range2 = b[1] + b[3]
    if a[0] >= range1 and a[1] >= range2:
        print("Nằm trong!")
    else:
        print("Nằm ngoài!")
is_inside([200, 120], [140, 60, 100, 200])

# Test case:
#   Nếu a[0] = 100 thì chuỗi in ra nằm ngoài là đúng, ngược lại hoặc báo lỗi là sai
#   Nếu a[0] = 200 thì chuỗi in ra nằm trong là đúng, ngược lại hoặc báo lỗi là sai