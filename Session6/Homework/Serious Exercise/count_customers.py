from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
# Count the number of customers group by refs

ref_kind = {
    "events":0,
    "wom":0,
    "ads":0
}

# get customers collection 
customer = db["customers"]

# Read documment 
all_customer = customer.find()

for kh in all_customer:
    if kh['ref'] in ref_kind:
        ref_kind[kh['ref']]+=1

for key, value in ref_kind.items():
    if value!=0:
        print("{0}: {1}".format(key, value))

# Matpolib
# 1 Chuẩn bị data
loai_ref = [ref_kind["events"], ref_kind["ads"], ref_kind["wom"]]

# 2. Chuẩn bị labels
ten_ref = ["Events", "WOM", "ADS"]

# Vẽ hình
pyplot.title("Customers group by Refs")
pyplot.pie(loai_ref, labels=ten_ref, autopct="%.1f%%", shadow=True, explode=[0,0.1,0.1])
pyplot.axis("equal")

# Show hàng
pyplot.show()