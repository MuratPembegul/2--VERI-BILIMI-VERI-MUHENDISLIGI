import requests
import pandas as pd

# 1. API'den Veri Çek
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# 2. JSON Verisini Pandas DataFrame'e Çevir
df = pd.DataFrame(data)

# 3. Veriyi Kaydet
df.to_csv("api_data.csv", index=False)

print("API veri çekme ve kaydetme tamamlandı! 🌍")
