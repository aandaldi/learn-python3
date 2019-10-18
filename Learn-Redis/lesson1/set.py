import redis

client = redis.Redis()

client.sadd('myset', 'Andik')
client.sadd('myset', 'Sergio')
client.sadd('myset', 'irfan')
client.sadd('myset', 'Zoya')


client.sadd('employee', 'Andik')
client.sadd('employee', 'Sergio')
client.sadd('employee', 'Lilipaly')
client.sadd('employee', 'Beni')
client.sadd('employee', 'Bayu')
client.sadd('employee', 'Boaz')
client.sadd('employee', 'Kurnia')
client.sadd('employee', 'Rizky')

print(client.smembers('myset'))                     #mencetak isi set
print(client.sismember('myset', 'Andik'))           #mengecek nilai, apakah value merupakan aggota dari set(sismember)
print(client.sismember('myset', 'Siroch Chatong'))

client.srem('myset', 'Zola')                        #menghapus suatu nilai
print(client.smembers('myset'))

print(client.sdiff('employee', 'myset'))            #melakukan operasi himpunan
print(client.sinter('employee', 'myset'))           #melakukan operasi himpunan
print(client.sunion('employee', 'myset'))           #melakukan operasi himpunan

client.delete('myset')
client.delete('employee')