# 📌 SQLite modülünü içe aktarıyoruz (Python'un yerleşik veritabanı modülü)
import sqlite3  

# 📌 1. Veri tabanı bağlantısı oluştur
# Eğer "ornek.db" adlı bir veri tabanı yoksa, otomatik olarak oluşturulur
conn = sqlite3.connect("ornek.db")  

# 📌 2. Veri tabanı ile iletişim kurmak için bir "imleç (cursor)" oluşturuyoruz
cursor = conn.cursor()  

# 📌 3. Yeni bir tablo oluştur (Eğer tablo yoksa)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS kullanicilar (
        id INTEGER PRIMARY KEY,  -- Birincil anahtar (ID)
        isim TEXT,  -- Kullanıcının adı (Metin)
        yas INTEGER  -- Kullanıcının yaşı (Tam sayı)
    )
''')

# 📌 4. Yeni veri ekleme fonksiyonu
def veri_ekle(isim, yas):
    cursor.execute("INSERT INTO kullanicilar (isim, yas) VALUES (?, ?)", (isim, yas))
    conn.commit()  # Değişiklikleri kaydet
    print(f"✅ Kullanıcı eklendi: {isim}, Yaş: {yas}")

# 📌 5. Tüm verileri listeleme fonksiyonu
def verileri_goster():
    cursor.execute("SELECT * FROM kullanicilar")
    veriler = cursor.fetchall()  # Tüm verileri al
    print("\n📌 Kullanıcı Listesi:")
    for veri in veriler:
        print(f"ID: {veri[0]}, İsim: {veri[1]}, Yaş: {veri[2]}")

# 📌 6. Veri güncelleme fonksiyonu
def veri_guncelle(id, yeni_isim, yeni_yas):
    cursor.execute("UPDATE kullanicilar SET isim = ?, yas = ? WHERE id = ?", (yeni_isim, yeni_yas, id))
    conn.commit()
    print(f"✅ Kullanıcı güncellendi: ID {id} -> Yeni İsim: {yeni_isim}, Yeni Yaş: {yeni_yas}")

# 📌 7. Veri silme fonksiyonu
def veri_sil(id):
    cursor.execute("DELETE FROM kullanicilar WHERE id = ?", (id,))
    conn.commit()
    print(f"❌ Kullanıcı silindi: ID {id}")

# 📌 8. Fonksiyonları test edelim
if __name__ == "__main__":
    veri_ekle("Ahmet", 25)  # Kullanıcı ekle
    veri_ekle("Ayşe", 30)  
    verileri_goster()  # Verileri listele
    
    veri_guncelle(1, "Ahmet Yılmaz", 26)  # ID 1 olan veriyi güncelle
    verileri_goster()
    
    veri_sil(2)  # ID 2 olan veriyi sil
    verileri_goster()

# 📌 9. İşimiz bitince bağlantıyı kapatıyoruz
conn.close()
