import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="Pmansi@4847",database='mydb')
curs=con.cursor()     # create cursor
curs.execute("select * from student;")

for row in curs:
    print(row[0],row[1],row[2])

con.close()

print("Finished...............")
