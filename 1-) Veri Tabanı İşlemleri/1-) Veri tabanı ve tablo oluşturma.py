import sqlite3

# Veri tabanını oluştur veya bağlan
conn = sqlite3.connect("veritabani.db")
cursor = conn.cursor()

# Kullanıcılar tablosunu oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS kullanicilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    soyad TEXT NOT NULL,
    yas INTEGER
)
''')

print("Tablo başarıyla oluşturuldu!")

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()
