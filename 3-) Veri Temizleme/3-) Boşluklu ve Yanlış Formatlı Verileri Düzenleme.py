import pandas as pd

# Örnek veri
data = {'İsim': [' Ali ', 'Veli', '  Ayşe', 'Mehmet  ', 'fatma '],
        'Telefon': ['(555) 123-45-67', '555-987-65-43', '5551234567', None, '555 654 32 10']}

df = pd.DataFrame(data)

# Boşlukları temizleme
df['İsim'] = df['İsim'].str.strip()

# Telefon numaralarını standart formata çevirme
df['Telefon'] = df['Telefon'].str.replace(r'\D', '', regex=True)  # Sadece rakamları bırak
df['Telefon'] = df['Telefon'].apply(lambda x: x if x and len(x) == 10 else None)  # Geçersizleri None yap

print(df)
