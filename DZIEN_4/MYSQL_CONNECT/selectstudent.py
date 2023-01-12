import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306,
                             database = 'dbtestowa')
cursorObject = db.cursor()
sqlsel = "SELECT name,nrstud FROM student"
cursorObject.execute(sqlsel)
print("dane studentów: ")
wynik = cursorObject.fetchall()
for rek in wynik:
    print(rek)


sqlsel = "SELECT name,nrstud FROM student WHERE nrstud > 70000"
cursorObject.execute(sqlsel)
print("dane studentów o wartości indeksu powyżej 70000: ")
wynik = cursorObject.fetchall()
for rek in wynik:
    print(rek)

db.close()
