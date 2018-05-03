from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# Down 1 video đơn lẻ
# dl.download(['https://www.youtube.com/watch?v=m5TIDDx57-0'])

# Download nhiều video
# dl.download(['https://www.youtube.com/watch?v=_8XrtrYFmtY', 'https://www.youtube.com/watch?v=qV_BDWUs4Vs', 'https://www.youtube.com/watch?v=op4B9sNGi0k'])

# option = {
#     'format':'best'
# }

# dl =YoutubeDL(option)
# dl.download(['https://www.youtube.com/watch?v=1kfUnvvRvMM'])

option = {
    'default_search': 'ytsearch',
    'max_downloads':1,
    'format': 'best'
}

dl  =YoutubeDL(option)
dl.download(['Phố Đêm'])