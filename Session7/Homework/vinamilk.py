from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
text_data = raw_data.decode('utf8')
soup = BeautifulSoup(text_data, "html.parser")
# print(soup.prettify())
table = soup.find("table", id = "tableContent")
trs = table.find_all("tr")

data  = []
for tr in trs:
    tds = tr.find_all('td')

    if tds != [] and tds[0].string != None:
        item = {
            "Tên": tds[0].string,
            "Quý 4 - 2016": tds[1].string,
            "Quý 1 - 2017": tds[2].string,
            "Quý 2 - 2017": tds[3].string,
            "Quý 3 - 2017": tds[4].string
        }
        data.append(item)
pyexcel.save_as(records=data, dest_file_name = "vinamilk.xlsx")
print("Success!")