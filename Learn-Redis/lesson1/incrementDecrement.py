import redis

client = redis.Redis()

client.set('visitor:home', 1)

for i in range(0,10):
    client.incr('visitor:home')
    print(client.get('visitor:home').decode('utf-8'))

print("=======")

for i in range(0,10):
    client.decr('visitor:home')
    print(client.get('visitor:home').decode('utf-8'))

client.delete('visitor:home')