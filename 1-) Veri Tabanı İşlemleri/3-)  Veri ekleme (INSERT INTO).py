import sqlite3

# Veri tabanına bağlan
conn = sqlite3.connect("veritabani.db")
cursor = conn.cursor()

# Yeni kullanıcı ekle
cursor.execute("INSERT INTO kullanicilar (ad, soyad, yas) VALUES (?, ?, ?)", 
               ("Ahmet", "Yılmaz", 25))

print("Veri başarıyla eklendi!")

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()
