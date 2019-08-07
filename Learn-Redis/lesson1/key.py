import redis

client = redis.Redis()
client.set('user:123', 'Aan' .encode('utf-8'))      #.encode and decode to remove byte on output(you can remove this)
user = client.get('user:123').decode('utf-8')

print(user)