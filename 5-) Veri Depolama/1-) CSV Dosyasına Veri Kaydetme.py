import csv

# Örnek veri
veriler = [
    ["Ad", "Soyad", "Yaş"],
    ["Murat", "Pembegül", 30],
    ["Ahmet", "Yılmaz", 25]
]

# CSV dosyasına yazma
with open("veri.csv", mode="w", newline="", encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerows(veriler)

print("CSV dosyası oluşturuldu!")
