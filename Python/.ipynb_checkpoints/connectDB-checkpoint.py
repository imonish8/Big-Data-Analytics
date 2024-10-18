import mysql.connector
"""

conn = mysql.connector.connect(host='localhost', user='root', password='Monish@16', database='MASTERCHEF')
print("Connected to database")
"""

try:
        dict={'host': 'localhost', 'user': 'root', 'password': 'Monish@16', 'database': 'MASTERCHEF' }
        conn = mysql.connector.connect (**dict)
        print ("connected to the Database")
        cur = conn. cursor ()
        #sql = "Create table hospital (hid int, hname varchar (20), location varchar (20)) "
       # cur.execute(sql)
        data = [(101, 'Chettinadu hospital', 'OMR'),
                (102,'Appollo hospital', 'Egmore'), (103, 'KCP hospital', 'Chennai'),
                (104, 'Bloom hospital', 'Velachery'), (105, 'Billroth hospital', 'Kilpauk') ]
       
        #sql1="insert into hospital(hid, hname, location) values(%s, %s, %s)"
        sql2="select * from hospital"
        cur. execute (sql2)
        #conn.commit ()
        print(cur.fetchall())
        print ("Inserted successfully")
except (mysql.connector.Error, IOError) as err:
        print ("Errorf}", err)
