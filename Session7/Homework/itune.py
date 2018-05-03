import pyexcel
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.apple.com/itunes/charts/songs/'

conn = urlopen(url)

raw_data  = conn.read()
text_data = raw_data.decode('utf8')

soup = BeautifulSoup(text_data, "html.parser")
div = soup.find("div", id = "main")
ul = div.find("ul")
li_list  = ul.find_all("li")

song_list = []

for li in li_list:
    a_song = li.h3.a
    a_song_name = a_song.string
    a_artis = li.h4.a
    a_artis_name = a_artis.string
    item = {
        "Songs":a_song_name,
        "Artis":a_artis_name
    }
    song_list.append(item)

pyexcel.save_as(records=song_list, dest_file_name = "itune.xlsx")
itune_file = open("itune.html", "w")
# lưu thô raw_data ghi wb = "write binary"
itune_file.write(text_data)
itune_file.close()

option = {
    'default_search': 'ytsearch',
    'max_downloads':1,
    'outtmpl': 'download/%(title)s.%(ext)s',
    'format': 'best'
}

dl  =YoutubeDL(option)

for song_item in song_list:
    a = str(song_item['Songs'])
    print(a)
    dl.download([a])