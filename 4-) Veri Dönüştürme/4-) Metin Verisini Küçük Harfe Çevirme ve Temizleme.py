import pandas as pd

# Örnek veri
data = {'Yorum': ['ÇOK Güzel BİR ürün!!!', 'Harika bir tasarım.', 'Fiyatı biraz pahalı ama iyi.']}

df = pd.DataFrame(data)

# Metinleri küçük harfe çevirme
df['Yorum'] = df['Yorum'].str.lower()

# Noktalama işaretlerini kaldırma
df['Yorum'] = df['Yorum'].str.replace(r'[^\w\s]', '', regex=True)

print(df)
