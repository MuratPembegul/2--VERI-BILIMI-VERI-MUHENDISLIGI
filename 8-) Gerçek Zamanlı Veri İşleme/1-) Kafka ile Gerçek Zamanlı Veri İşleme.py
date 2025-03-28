from kafka import KafkaProducer  
import json  
import time  

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

topic = "real_time_data"

# Gerçek zamanlı olarak veri gönderelim
for i in range(10):
    data = {"id": i, "value": i * 2}
    producer.send(topic, value=data)
    print(f"Gönderildi: {data}")
    time.sleep(1)  # 1 saniyede bir veri gönder
