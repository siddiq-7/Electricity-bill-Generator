import mysql.connector as sql
conn = sql.connect(
  host="localhost",
  user="root",
  password="1234"
)

if conn.is_connected():
    print("sucessfully connected")

conn.cursor().execute("CREATE DATABASE electricity_data1")
print("Database Successfully Created")
conn.cursor().execute("USE electricity_data1")
conn.cursor().execute('create table log_in(cust_name  varchar(65), account_no  int, password int)')
print("Log_in_table created")
conn.cursor().execute('create table consumer_details(f_name varchar(65),units int,bill int,cust_name varchar(65), phone_no bigint)')
print("Consumer_details created")
conn.commit()
print("DONE")
