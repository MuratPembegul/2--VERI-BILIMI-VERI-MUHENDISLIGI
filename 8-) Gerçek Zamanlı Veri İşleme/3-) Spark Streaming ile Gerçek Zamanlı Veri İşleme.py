from pyspark.sql import SparkSession  
from pyspark.sql.functions import explode, split  

# Spark oturumunu başlat
spark = SparkSession.builder.appName("RealTimeProcessing").getOrCreate()

# Gerçek zamanlı veriyi (örneğin bir TCP portundan) oku
df = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

# Gelen veriyi böl ve kelime kelime göster
words = df.select(explode(split(df.value, " ")).alias("word"))

# Sonuçları göster
query = words.writeStream.outputMode("append").format("console").start()

query.awaitTermination()
