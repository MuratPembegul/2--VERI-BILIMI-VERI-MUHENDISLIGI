import sqlite3

# Veritabanı bağlantısı oluştur
conn = sqlite3.connect("veri.db")
cursor = conn.cursor()

# Tablo oluştur
cursor.execute("""
CREATE TABLE IF NOT EXISTS kisiler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT,
    yas INTEGER
)
""")

# Veri ekle
cursor.execute("INSERT INTO kisiler (ad, yas) VALUES (?, ?)", ("Murat", 30))

# Kaydet ve kapat
conn.commit()
conn.close()

print("SQLite veritabanına veri eklendi!")
