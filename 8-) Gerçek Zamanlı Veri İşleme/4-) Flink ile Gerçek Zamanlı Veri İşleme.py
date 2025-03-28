from pyflink.datastream import StreamExecutionEnvironment  

env = StreamExecutionEnvironment.get_execution_environment()

# Kaynak (Gerçek zamanlı veri akışı)
source = env.from_collection([(1, "Veri 1"), (2, "Veri 2")])

# Transformasyon (Verileri büyük harfe çevir)
processed = source.map(lambda x: (x[0], x[1].upper()))

# Çıktıyı ekrana yazdır
processed.print()

# Çalıştır
env.execute("Gerçek Zamanlı Veri İşleme")
