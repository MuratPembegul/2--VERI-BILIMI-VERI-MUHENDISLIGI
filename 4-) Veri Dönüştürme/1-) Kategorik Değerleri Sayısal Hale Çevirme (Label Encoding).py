import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Örnek veri
data = {'Şehir': ['İstanbul', 'Ankara', 'İzmir', 'İstanbul', 'Ankara']}

df = pd.DataFrame(data)

# Label encoding uygulama
encoder = LabelEncoder()
df['Şehir_Kod'] = encoder.fit_transform(df['Şehir'])

print(df)
