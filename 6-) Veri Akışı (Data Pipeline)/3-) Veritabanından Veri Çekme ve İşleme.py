import sqlite3
import pandas as pd

# 1. Veritabanına Bağlan
conn = sqlite3.connect("veritabani.db")

# 2. SQL Sorgusu ile Veriyi Çek
query = "SELECT * FROM musteriler"
df = pd.read_sql(query, conn)

# 3. Veriyi İşle (örn: isimleri büyük harfe çevir)
df["isim"] = df["isim"].str.upper()

# 4. Yeni İşlenmiş Veriyi Kaydet
df.to_sql("musteriler_yeni", conn, if_exists="replace", index=False)

print("Veritabanı veri işleme tamamlandı! 🏦")

# Bağlantıyı Kapat
conn.close()
