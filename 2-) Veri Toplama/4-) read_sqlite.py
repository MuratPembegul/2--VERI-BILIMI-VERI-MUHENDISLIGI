import sqlite3

db_adi = "veritabani.db"
conn = sqlite3.connect(db_adi)
cursor = conn.cursor()

cursor.execute("SELECT * FROM kullanicilar LIMIT 5")  # Örnek tablo: kullanicilar
veriler = cursor.fetchall()

for veri in veriler:
    print(veri)

conn.close()
