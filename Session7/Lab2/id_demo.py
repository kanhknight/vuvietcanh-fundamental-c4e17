import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs/"
conn  = urlopen(url)
# 1.2 Read raw data
raw_data  = conn.read()

# 1.3 Decode
text=raw_data.decode('utf8')

soup = BeautifulSoup(text, "html.parser")
roi_area = soup.find("div", id = "main")
print(roi_area)
# trong đó id = "main" là tên của id trong ROI