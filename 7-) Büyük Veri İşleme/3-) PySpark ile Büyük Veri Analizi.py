from pyspark.sql import SparkSession  

# Spark oturumu başlat
spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()

# Büyük CSV dosyasını okuma
df = spark.read.csv("big_data.csv", header=True, inferSchema=True)

# Veriyi gösterme
df.show(5)
