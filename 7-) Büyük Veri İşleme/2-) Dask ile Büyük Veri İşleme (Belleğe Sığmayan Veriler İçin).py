import dask.dataframe as dd  

# Büyük CSV dosyasını Dask ile okuma
df = dd.read_csv("big_data.csv")

# Hızlı analiz (Dask tembel çalışır, hesaplamak için compute() kullanılır)
print(df.describe().compute())
