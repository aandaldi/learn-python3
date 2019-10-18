import json
import redis

client = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

#
# restaurant_484272 = {
#     "name": "Ravagh",
#     "type": "Persian",
#     "address": {
#         "street": {
#             "line1": "11 E 30th St",
#             "line2": "APT 1",
#         },
#         "city": "New York",
#         "state": "NY",
#         "zip": 10016,
#     }
# }

## JSON TO REDIS
# client.set(484272, json.dumps(restaurant_484272))
#
# print(restaurant_484272)
# print('=========')
# # pprint(json.loads(client.get(484272)))
# print(json.dumps(restaurant_484272, indent=4))
# print ("-------------------ini get ------------------------")
# print(client.get(484272))

print("==============TEST STORE JSON TO REDIS==================")

data=[]
for x in range(2):
   id = x
   nama = 'aan{}'.format(x)
   string = {"id":id, "nama":nama}
   data.append(string)
   print(data)
mydata = {"data": data}
print("ini my data", mydata, "\n")
print("======================ini isi redis============")
client.lpush('us', mydata)
# print(client.lrange('us',0,10))
print(json.dumps(client.lrange('us',0, 10)))
client.lpop('us')


