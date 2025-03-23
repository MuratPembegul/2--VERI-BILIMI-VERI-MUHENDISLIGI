import sqlite3

# Veri tabanına bağlan
conn = sqlite3.connect("veritabani.db")
cursor = conn.cursor()

# Kullanıcıları getir
cursor.execute("SELECT * FROM kullanicilar")
veriler = cursor.fetchall()

# Sonuçları ekrana yazdır
for satir in veriler:
    print(satir)

# Bağlantıyı kapat
conn.close()
