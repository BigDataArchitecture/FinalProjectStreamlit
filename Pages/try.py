import pymongo

client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
print(client["News"])
query = {'news_Country': {'$in': ['Australia']}, 'news_topic': {'$in': ['Business']}}
db = client["News"]
collection = db["GoogleAPI_links"]
mydoc = collection.find(query)

for i in mydoc:
    print(i['news_link'])
