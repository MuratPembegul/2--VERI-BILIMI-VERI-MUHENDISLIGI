import pandas as pd  

# Büyük bir CSV dosyasını parça parça okuma (chunk size kullanarak)
chunk_size = 100000  # 100 bin satırda bir okuma
csv_file = "big_data.csv"

for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    print(chunk.head())  # Her parçanın ilk 5 satırını göster
