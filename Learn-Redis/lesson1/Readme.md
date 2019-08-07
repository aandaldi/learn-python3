##Tentang Redis
- Tipe data:
    - String
        - SET
            - untuk menginisialisasi sebuah key dan value
        - GET/GETRANGE
            - untuk mengambil sebuah key dan  (*hanya mengembalikan tipe String)
        - STRLEN 
            - untuk menghitung panjang karakter value dari sebuah key
        - SETEX
            - untuk mengeset value dari sebuah key dengan waktu tertentu
        - DEL
            - untuk menghapus value dari sebuah key
        - GETSET
            - untuk mengupdate/insert value dari sebuah key
        - LPUSH
            - untuk membuat list dari sebuah value, cara menampilkannya dengan LRANGE 0 - X (* x = integer)
        - SADD
            - untuk membuat set(koleksi) untuk sebuah key, cara menampilkannya dengan SMEMBER key
        - ZADD
            - kumpulan elemen string, skor dapat dapat berulang tapi value bersifat unik(untuk mempermudah cluster), cara menampilkannya dengan ZRANGEBYSCORE key *range key
        - EXISTS
            - untuk mengecek apakah key telah tersimpan, bentuk balikan berupa boolean.
        - EXPIRE
            - untuk menset waktu kadaluarsa sebuah key dan value, setelahnya akan dihapus
        - EXPIREAT
            - untuk Expired menggunakan UNIX timestamp 
        - MOVE  
            - digunakan memindahkan database contoh (MOVE KEY_NAME DESTINATION_DATABASE)
        - PERSIS
            - digunakan untuk membuat key yang tetap ada tanpa ada waktu expired
        - RENAME
            - digunakan untuk mengganti nama key (RENAME OLD_KEY_NAME NEW_KEY_NAME)
        - TYPE
            - mengecek tipe key
        - APPEND
            - menambahkan value kedalam sebuah key
    - Hash
        - HKEYS
            - digunakan untuk mendapatkan tabel hash dari semua nama field
        - HMGET 
            - Hmget perintah mengembalikan tabel hash, satu atau lebih nilai untuk bidang tertentu
        - HMSET
            - Hmset sementara sejumlah lapangan-nilai (bidang - nilai) dari set ke tabel hash.
            - HMSET KEY_NAME FIELD1 VALUE1 ...FIELDN VALUEN
        - HSET/HSETNX
            - Hset Perintah ini digunakan untuk hash table bidang tugas, sedang HSENX tidak akan di jalankan apabila bidang sudah ada
            - HSET KEY_NAME FIELD VALUE 
        - 
    - List
        - BLPOP key1 [key2] batas waktu 
            - Dan keluar dari elemen pertama dari daftar, jika daftar tidak daftar elemen akan diblokir sampai batas waktu atau tanggal dapat ditemukan dalam elemen pop-up.
        - key1 BRPOP [key2] batas waktu 
            - Dan keluar dari elemen terakhir dari daftar, jika daftar tidak daftar elemen akan diblokir sampai batas waktu atau tanggal dapat ditemukan dalam elemen pop-up.
        - BRPOPLPUSH batas waktu source destination 
            - Pop nilai dari daftar, elemen pop ke dalam daftar lain dan mengembalikannya, jika tidak ada unsur daftar akan memblokir sampai batas waktu atau sampai daftar dapat ditemukan dalam elemen pop-up.
        - indeks kunci LINDEX 
            - Dapatkan daftar elemen dengan indeks
        - LINSERT kunci SEBELUM | nilai poros SETELAH 
            - Dalam daftar elemen sebelum atau sesudah elemen insert
        - kunci LLEN 
            - Dapatkan daftar panjang
        - kunci LPOP 
            - Dan keluar dari elemen pertama dari daftar
        - LPUSH kunci nilai1 [nilai2] 
            - Satu atau lebih nilai ke dalam kepala daftar
        - nilai kunci LPUSHX 
            - Satu atau lebih nilai ke dalam daftar kepala yang ada
        - LRANGE tombol mulai berhenti 
            - Dapatkan daftar unsur-unsur dalam kisaran tertentu
        - LREM kunci nilai hitungan 
            - Hapus daftar elemen
        - LSET nilai indeks kunci 
            - Mengatur nilai elemen dari daftar dengan indeks
        - LTRIM tombol mulai berhenti 
            - Untuk daftar trim (trim), yaitu, membuat daftar hanya elemen selang retensi yang ditentukan, unsur ini tidak ditentukan dalam rentang akan dihapus.
        - kunci RPOP 
            - Hapus dan memperoleh daftar elemen terakhir
        - source destination RPOPLPUSH 
            - Menghapus elemen terakhir dari daftar, dan menambahkan elemen ke daftar lain dan kembali
        - RPUSH kunci nilai1 [nilai2] 
            - Tambahkan satu atau lebih nilai dalam daftar
        - nilai kunci RPUSHX 
            - Menambahkan nilai pada daftar yang ada

## Learn redis using python
######documentation on (~ https://redis-py.readthedocs.io/en/latest/ ~)

1. Install redis on your OS
2. Install redis package on your python environment
3. create connection file to redish(connect.py)
###Operasi dasar pada redis
- menyimpan key dan value (contoh pada file key.py)
- membuat key dengan expire time (key_expire.py)
- increment and decrement operate (incrementDecrement.py)
- menjalankan methode has. `hash adalah struktur kompleks mirip JSON` (hash.py)
- operasi list
    