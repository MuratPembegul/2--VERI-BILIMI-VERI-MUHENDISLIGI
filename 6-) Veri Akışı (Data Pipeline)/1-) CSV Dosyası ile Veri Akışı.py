import pandas as pd

# 1. Veri Kaynağını Oku
df = pd.read_csv("data.csv")

# 2. Boş Verileri Temizle
df_cleaned = df.dropna()

# 3. Yeni Temizlenmiş Veriyi Kaydet
df_cleaned.to_csv("cleaned_data.csv", index=False)

print("CSV veri temizleme tamamlandı! 🚀")
