import pandas as pd

# Örnek veri
data = {'Ürün': ['Telefon', 'Laptop', 'Tablet'],
        'Fiyat (TL)': [5000, 10000, 3000]}

df = pd.DataFrame(data)

# Döviz kuru (örnek olarak 1 USD = 38 TL)
usd_kuru = 38

# TL fiyatını USD'ye çevirme
df['Fiyat (USD)'] = df['Fiyat (TL)'] / usd_kuru

print(df)
