from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient("mongodb://localhost:27017/")
db = client["veritabanim"]
koleksiyon = db["kisiler"]

# Örnek veri ekleme
veri = {"ad": "Murat", "yas": 30}
koleksiyon.insert_one(veri)

print("MongoDB'ye veri eklendi!")
