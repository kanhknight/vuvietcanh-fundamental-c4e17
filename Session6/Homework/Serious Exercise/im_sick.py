from gmail import *
from random import choice
from datetime import *

gmail = GMail("canhvuico@gmail.com", "vuvietcanh88")

diachi = ["kanhknight@gmail.com"]

html_template = "<b>Em chào thầy ạ!</b></br> Em biết hôm nay trời rất là đẹp nhưng không may em bị {{ly_do}}!</br> Nên giờ em viết mail này kính mong Thầy cho e được offline buổi ngày hôm nay!"
ly_do_list = ["Viêm màng túi", "hôi nách", "đau ruột cong", "vi rút tấn công", "Đau CPU"]

while True:
    send_time = datetime.now()
    if send_time.hour == 14 and send_time.minute == 20 and send_time.second == 10:
        for i in diachi:
            ly_do = choice(ly_do_list)
            html_content = html_template.replace("{{ly_do}}", ly_do)
            msg = Message('Thư xin nghỉ ốm!', to = i, html= html_content)
            gmail.send(msg)
            print("Đã gửi thư tới: ",i)