#  insert, update, delete

insert_query="Insert into student values(4,'m',50)"
update_query= "update student set sname='n' where SNO=4;"
delete_query="delete from student where sno=4;"

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="Pmansi@4847",database='mydb')
curs=con.cursor()     # create cursor
# curs.execute(insert_query)   # execute query through cursor
# curs.execute(update_query)
curs.execute(delete_query)
con.commit()  # commit transaction
con.close()

print("Finished...............")
