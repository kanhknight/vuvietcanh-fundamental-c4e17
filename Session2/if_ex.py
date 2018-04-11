yob = int(input("Nhập vào năm sinh của bạn: "))
tuoi = 2018 - yob
if tuoi < 10:
    print("Baby")
elif tuoi < 18:
    print("Tuổi Teen")
else:
    print("Adult")