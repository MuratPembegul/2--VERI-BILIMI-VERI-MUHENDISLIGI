import pandas as pd

# Örnek veri
data = {'Ad': ['Ali', 'Veli', 'Ayşe', None, 'Mehmet'],
        'Yaş': [25, None, 30, 22, None],
        'Maaş': [5000, 6000, None, 7000, 8000]}

df = pd.DataFrame(data)

# Eksik değerleri doldurma (ortalama ile)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Eksik isimleri 'Bilinmiyor' ile doldurma
df['Ad'].fillna('Bilinmiyor', inplace=True)

print(df)
