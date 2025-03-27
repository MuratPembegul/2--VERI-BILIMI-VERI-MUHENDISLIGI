import json

# Örnek veri
veri = {
    "isim": "Murat",
    "yaş": 30,
    "şehir": "Konya"
}

# JSON dosyasına yazma
with open("veri.json", "w", encoding="utf-8") as dosya:
    json.dump(veri, dosya, indent=4)

print("JSON dosyası oluşturuldu!")
