import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='root',database='mas_data')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Successfull connection!")