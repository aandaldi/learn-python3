import redis

client = redis.Redis()

client.lpush('tim_bola', 'Persib')
client.lpush('tim_bola', 'Persipura')
client.lpush('tim_bola', 'Arema Cronus')
client.lpush('tim_bola', 'Madura United').decode('utf-8')

print(client.lrange('tim_bole', 0, -1))

client.rpush('tim_bola', 'Mitra Kukar')
client.rpush('tim_bola', 'Semen Padang')
client.rpush('tim_bola', 'Persija')
client.rpush('tim_bola', 'PSM Makassar')

print(client.lrange('tim_bola', 0, -1))
print(client.llen('tim_bola'))

print(client.lindex('tim_bola', 1))
print(client.lindex('tim_bola', 2))
print(client.lindex('tim_bola', 3))
print(client.lindex('tim_bola', 4))
print(client.lindex('tim_bola', 5))
print(client.lindex('tim_bola', 10))
print("============")

client.lpop('tim_bola')
print(client.lrange('tim_bola', 0, -1))
print("#################")

client.rpop('tim_bola')
print(client.lrange('tim_bola', 0, -1))
print('==============')

client.delete('tim_bola')