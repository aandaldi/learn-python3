#using PostgreSql

import psycopg2

#connection
try:
    connection = psycopg2.connect(user = "localpostgre",
                                  password = "localpostgre",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "staff")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
else:
    print("connection to database succesful!")


cursor = connection.cursor()

# CREATE TABLE ON DATABASE
# cursor.execute(
#     '''create table mystaff.employees(
#         id int primary key not null,
#         first_name varchar(25) not null,
#         last_name varchar(25) not null,
#         department varchar(25) not null,
#         phone varchar(25),
#         address varchar(50),
#         salary int
#     );'''
# )

# INSERT INTO TABLE
# cursor.execute(
#     '''
#     insert into mystaff.employees(id, first_name, last_name, department, phone, address, salary)\
#     values (1, 'John', 'Smith', 'Sales', '090909090', '1st Street,  Miami', '5000'),\
#            (2, 'Ace', 'Batu', 'IT', '0903', '2st Street,  Ny', '5040'),\
#            (3, 'Roki', 'Rahmat', 'Logistics', '09867868', '3st Street,  LA', '7876')\
#     ;'''
# )

# Querying THE DATABASE
# cursor.execute("select * from mystaff.employees;")
#
# records_one= cursor.fetchone()
# records_many= cursor.fetchmany(size=2)
# records = cursor.fetchall()
#
#
# for many in records_many:
#     print(many)
#
# for one in records_one:
#     print(one)
#
# for records in records:
#     print(records)

# APPEND DATA FROM SOME FILE TO DATABASE
f = open("../SimpleProjects/MiddleLevel/employees.txt")

records = []
for i in f. readlines():
    records.append(i.split("/ "))

print (records)

#insert the data
try:
    for i in records:
        cursor.execute("insert into mystaff.employees"
                       "(id, first_name, last_name, department, phone, address, salary)"
                       "values(%s, %s, %s, %s, %s, %s, %s);",(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
else:
    print("Records inserted successsfully!\n")


connection.commit()
connection.close()
