import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306,
                             database = 'dbtestowa')
cursorObject = db.cursor()
sqlins = "INSERT INTO student(name,nrstud) VALUES(%s,%s)"
val = [
    ("Leon",63454),
    ("Olga",745645),
    ("Jan",8768876),
    ("Beata",622322),
    ("Eryk",623233),
    ("Nadia",132323),
]
cursorObject.executemany(sqlins,val)
db.commit()
print(f"{cursorObject.rowcount} rekordów osadzono")
db.close()
