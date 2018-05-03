import pyexcel
from urllib.request import urlopen
# beautiful4soup
from bs4 import BeautifulSoup
# 1. Download
# 2. Find ROI - (Region of Interest)
# 3. Extract Info

url = "http://dantri.com.vn"
# 1.1 Open connection
conn  = urlopen(url)

# 1.2 Read raw data
raw_data  = conn.read()

# 1.3 Decode
text=raw_data.decode('utf8')

# print(text)
    # dan_tri_file = open("dantri.html", "w")
# lưu thô raw_data ghi wb = "write binary"
    # dan_tri_file.write(text)
    # dan_tri_file.close()

# Tìm ROI
soup = BeautifulSoup(text, "html.parser")
# print(soup.prettify()) # Làm đẹp lại code !

ul = soup.find("ul", "ul1 ulnew")

li_list = ul.find_all("li")

# li = li_list[0]
item_list = []

for li in li_list:
    a = li.h4.a # walking
    title = a.string # Cách in string content
    # print(title)
    link = url + a['href']
    # print(link)
    # print("__________________________")
    item = {
        "Link": link,
        "Title": title
    }
    item_list.append(item)
print(item_list)

pyexcel.save_as(records=item_list, dest_file_name = "ok.xlsx")
# print(a.prettify())

# Get string and content
# title = a.string
# print(title)
# link = url + a['href']
# print(link)