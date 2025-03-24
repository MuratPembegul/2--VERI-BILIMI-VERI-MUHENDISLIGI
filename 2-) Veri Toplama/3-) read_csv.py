import pandas as pd

dosya_adi = "veriler.csv"

try:
    df = pd.read_csv(dosya_adi)
    print(df.head())  # İlk 5 satırı göster
except FileNotFoundError:
    print(f"{dosya_adi} dosyası bulunamadı.")
