import redis

try:
    client  = redis.Redis()
    print("Connection to redis has beend established")
except Exception as e:
    print ("Cannot connect to redis")
    print (e)