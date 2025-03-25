import pandas as pd

# Örnek veri
data = {'Yaş': [25, -3, 150, 30, 40, None, 22],
        'Maaş': [5000, 6000, -1000, 7000, None, 8000, 200000]}

df = pd.DataFrame(data)

# Mantıksız yaşları filtreleme (0-100 arası)
df = df[(df['Yaş'] > 0) & (df['Yaş'] < 100)]

# Maaşı negatif olanları kaldırma
df = df[df['Maaş'] > 0]

print(df)
