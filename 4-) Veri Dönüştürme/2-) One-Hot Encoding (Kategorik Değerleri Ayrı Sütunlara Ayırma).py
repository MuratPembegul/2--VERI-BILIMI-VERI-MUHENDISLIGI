import pandas as pd

# Örnek veri
data = {'Renk': ['Kırmızı', 'Mavi', 'Yeşil', 'Mavi', 'Kırmızı']}

df = pd.DataFrame(data)

# One-hot encoding işlemi
df_encoded = pd.get_dummies(df, columns=['Renk'])

print(df_encoded)
