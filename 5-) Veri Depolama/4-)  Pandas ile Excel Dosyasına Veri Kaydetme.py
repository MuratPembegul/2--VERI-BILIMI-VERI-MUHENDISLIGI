import pandas as pd

# Örnek veri
veriler = {
    "Ad": ["Murat", "Ahmet", "Zeynep"],
    "Yaş": [30, 25, 28]
}

df = pd.DataFrame(veriler)

# Excel dosyasına kaydetme
df.to_excel("veri.xlsx", index=False)

print("Excel dosyası oluşturuldu!")
