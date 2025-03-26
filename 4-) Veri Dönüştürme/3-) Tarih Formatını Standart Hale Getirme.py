import pandas as pd

# Örnek veri
data = {'Tarih': ['01-02-2023', '2023/03/05', '05.04.2023', '2023-06-07']}

df = pd.DataFrame(data)

# Tarihleri standart formata çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'], dayfirst=True)

print(df)
