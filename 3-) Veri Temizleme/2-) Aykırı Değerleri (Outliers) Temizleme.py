import pandas as pd
import numpy as np

# Örnek veri (Bazı aykırı değerler var)
data = {'Gelir': [5000, 6000, 7000, 200000, 5500, 5800, 6100, 7200, 80000]}

df = pd.DataFrame(data)

# Aykırı değerleri tespit etme (IQR yöntemi)
Q1 = df['Gelir'].quantile(0.25)
Q3 = df['Gelir'].quantile(0.75)
IQR = Q3 - Q1

alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

# Aykırı değerleri temizleme
df = df[(df['Gelir'] >= alt_sinir) & (df['Gelir'] <= ust_sinir)]

print(df)
