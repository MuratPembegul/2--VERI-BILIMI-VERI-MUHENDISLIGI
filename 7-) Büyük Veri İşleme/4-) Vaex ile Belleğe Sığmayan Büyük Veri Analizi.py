import vaex  

# Büyük CSV dosyasını Vaex ile okuma
df = vaex.open("big_data.csv")

# Hızlı analiz (çok büyük verilerde bile çalışır)
print(df.describe())
