import redis

client = redis.Redis()

client.hset('users:123', 'name', 'aan'.encode('utf-8'))
client.hset('users:123', 'email', 'aan@mail.com'.encode('utf-8'))
client.hset('users:123', 'dob', '1990-09-09'.encode('utf-8'))

print(client.hgetall('users:1234'))

print(client.hget('users:123', 'name'))
print(client.hget('users:123', 'email'))
print(client.hget('users:123', 'dob'))

print(client.hkeys('users:123'))        #hanya mengambil value
print(client.hvals('users:123'))        #hanya mengambil value

print(client.hlen('users:123'))
print(client.hexists('users:123', 'email'))
print(client.hexists('users:123', 'website'))

client.hexists('users:123','dob')
print(client.hexists('users:123','dob'))

client.delete('users:123')
