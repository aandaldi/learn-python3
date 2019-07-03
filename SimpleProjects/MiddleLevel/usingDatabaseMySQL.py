#using MySQL

import pymysql

#connection
from docutils.nodes import paragraph

try:
    connection = pymysql.connect(user = "local",
                                 password = "local",
                                 host = "127.0.0.1",
                                 db = "python_mysql")
except (Exception, pymysql.Error) as error:
    print("Error while connecting to PostgreSQL", error)
else:
    print("connection to database succesful!")


cursor = connection.cursor()

query = '''create table python_mysql.employees(
        id int primary key not null,
        first_name varchar(25) not null,
        last_name varchar(25) not null,
        department varchar(25) not null,
        phone varchar(25),
        address varchar(50),
        salary int
    );'''

cursor.execute(query)


connection.commit()
connection.close()
