import redis  

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe("real_time_channel")

for message in pubsub.listen():
    if message["type"] == "message":
        print(f"Alınan Veri: {message['data']}")
