import pandas as pd

# Örnek veri
data = {'ID': [1, 2, 3, 3, 4, 5, 5, 6],
        'Ad': ['Ali', 'Veli', 'Ayşe', 'Ayşe', 'Mehmet', 'Fatma', 'Fatma', 'Zeynep']}

df = pd.DataFrame(data)

# Yinelenen verileri temizleme
df = df.drop_duplicates()

print(df)
