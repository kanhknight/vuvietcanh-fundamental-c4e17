from pymongo import MongoClient

# 1. Connect to database server
uri = "mongodb://admin:admin@ds235827.mlab.com:35827/c4e17"
client = MongoClient(uri)

# 2. Get default database
db = client.get_default_database()

# 3. Get blog collection
blog = db["blog"]

# 4. Write a new blog
post = {
    "title":"Nghiệp code dạo!",
    "content":"Code mà như không code!!"
}

post = {
    "title":"Hôm nay trời mưa!",
    "content":"Lại ở nhà code!!"
}
# 5. Insert documment 
# blog.insert_one(post)

# 6. Read documment 
all_post = blog.find()
for post in all_post:
    print(post)

# 7. Update documment

all_post = blog.update()
