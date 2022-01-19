# for mysql connection with python, we need to install a plugin from PIP3 called mysql-connector-python
# we have connect method in mysql package which accepts **kwards and we need to pass the required info
# once the connection opened, we use the connect object and create a cursor
# we use the cursor object to execute the query
# from that cursot you can iterate the loop and get the table details or we can use fetch methods availabe
# cursor.description is used to get the complete information of columns in the results table
# from the cursor we iterate the key(column details) and value(result) using enumerate function
# and after getting the columns and values data in to separate list
# we can make it as a dictionary using dict and zip to combine the 2 lists

import mysql.connector
class sqlTest:
    def connection_Test(self):
        self.sqlCon = mysql.connector.connect(host="localhost",user="root",password="test",database="jdbctest")
        query="select * from gmailform;"
        mycursor=self.sqlCon.cursor()
        mycursor.execute(query)
       # for row in mycursor:
        #    print(row)
        return  mycursor

    def close_connection(self):
        self.sqlCon.close()

test=sqlTest()
cursor=test.connection_Test()


columns=cursor.description
fields=[]
result=[]
for value in cursor.fetchall():
    for (key,kValue) in enumerate(value):
        fields.append(columns[key][0])
        result.append(kValue)
dictValues=dict(zip(fields,result))
print(dictValues.get("firstName"))
test.close_connection()