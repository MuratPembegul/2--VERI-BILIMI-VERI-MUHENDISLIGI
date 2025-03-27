import pandas as pd

# Örnek veri
data = {'Ürün Adı': ['Telefon', 'Laptop', 'Tablet'],
        ' Satış Tutarı ': [5000, 10000, 3000]}

df = pd.DataFrame(data)

# Sütun adlarını temizleme (boşlukları kaldır, küçük harfe çevir, Türkçe karakterleri değiştir)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('ı', 'i')

print(df)
