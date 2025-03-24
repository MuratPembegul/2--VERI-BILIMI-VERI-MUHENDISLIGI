import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"İlk 5 veri:\n{data[:5]}")
else:
    print("API'den veri alınamadı.")
