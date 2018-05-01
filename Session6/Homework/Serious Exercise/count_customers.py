from pymongo import MongoClient
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