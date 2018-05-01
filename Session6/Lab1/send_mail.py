from gmail import *
from random import choice
gmail = GMail('canhvuico@gmail.com','vuvietcanh88')
address = [
# "chilehnuehsgs@gmail.com",
# "chung.hitc97@gmail.com",
# "nguyentrungnguyenth14@gmail.com",
# "daoduc1910@gmail.com",
# "quangtruong23121996@gmail.com",
# "oanh.nguyenkim@vndirect.com.vn",
# "hangan9211@gmail.com",
# "dungftu.4t@gmail.com",
# "nhatminhmrur51971@gmail.com",
# "levinhphuc37@gmail.com",
# "lmthanh2011@gmail.com",
# "dattran1997@gmail.com",
# "leducanh300795@gmail.com",
# "luongnhuyen@gmail.com",
"kanhknight@gmail.com"
# "queensland1990@gmail.com",
# "tanvn.nevents@gmail.com",
# "hieu.trung.nguyen90@gmail.com",
# "7loveforu10@gmail.com",
# "duchn.sic@gmail.com",
# "tunghr.des@gmail.com",
# "c4e.201708@gmail.com"
]
html_template = "<b>Hello! {{chao}}</b> "
hello_list = ["Chào em!", "Chào Anh!", "Chào chị!", "Chào ông!", "Chào Bà!"]
chao = choice(hello_list)
html_contents = html_template.replace("{{chao}}", chao)

while True:
    for i in address:
        msg = Message('Test Message 2',to=i,html=html_contents)
        gmail.send(msg)
        print(i)