import redis
import time

client  = redis.Redis()
client.set('cart:12345', "{\"nama\":\"shampoo jwitsal\", \"amount\":\"10\"}".encode('utf-8'))
client.expire('cart:12345', 10)

run = True
while run:
    cart = client.get('cart:12345').decode('utf-8')
    print (cart)

    ttl = client.ttl('cart:12345')
    print(ttl)

    if ttl < 0:
        run = False

    time.sleep(1)