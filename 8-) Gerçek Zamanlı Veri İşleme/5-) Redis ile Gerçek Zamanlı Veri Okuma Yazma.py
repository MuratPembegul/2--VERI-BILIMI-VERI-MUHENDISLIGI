import redis  
import time  

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

while True:
    r.publish("real_time_channel", "Gerçek zamanlı veri akışı")
    print("Veri Gönderildi!")
    time.sleep(1)
