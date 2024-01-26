from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.inserm_articles
collection = db.articles
collection.create_index([('title', 1)])
