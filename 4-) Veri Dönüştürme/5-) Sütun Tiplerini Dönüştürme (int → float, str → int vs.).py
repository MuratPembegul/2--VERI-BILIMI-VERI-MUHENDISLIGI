import pandas as pd

# Örnek veri
data = {'Ürün_ID': ['101', '102', '103', '104'],
        'Fiyat': ['120.5', '89.99', '150', '200.75']}

df = pd.DataFrame(data)

# String olan sütunları sayısal hale çevirme
df['Ürün_ID'] = df['Ürün_ID'].astype(int)
df['Fiyat'] = df['Fiyat'].astype(float)

print(df)
