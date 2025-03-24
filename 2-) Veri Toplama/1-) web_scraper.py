import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # Buraya gerçek bir site ekleyebilirsin
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

basliklar = soup.find_all("h2")  # Tüm <h2> başlıklarını çekelim

for i, baslik in enumerate(basliklar, 1):
    print(f"{i}: {baslik.text}")
