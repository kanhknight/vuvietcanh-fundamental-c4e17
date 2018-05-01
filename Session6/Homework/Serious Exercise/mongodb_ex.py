from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
post_content = db["posts"]
html_content= '\nMôi hôn chan chứa ta trao \nYêu thương thắm thiết dạt dào người ơi\nTrải bao năm tháng tuyệt vời\nNghĩa tình chồng vợ muôn đời sắc son \nBên nhau hạnh phúc vẹn tròn\nVòng tay ấm áp … môi hôn đậm tình\nBên nhau dệt mộng thắm xinh\nCho đời thơm ngát lung linh đất trời\nEm bên anh mãi muôn đời\nTháng ngày bền chặt rộn lời ái ân\nTình say muôn thuở ngọt lành\nÊm đềm chung thủy yến oanh nồng nàn\nYêu thương vút tận mây ngàn\nĐôi bờ môi thắm chứa chan cõi lòng…\nHồn lâng say chốn phiêu bồng\nHương tình nồng đượm …dập dồn đôi tim…'
post = {
    "title":"TÌNH SAY!",
    "author":"Vũ Cảnh đi copy",
    "content": html_content
}

post_content.insert_one(post)