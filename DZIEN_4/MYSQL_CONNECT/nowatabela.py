import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306,
                             database = 'dbtestowa')
cursorObject = db.cursor()
nowatabela = "CREATE TABLE IF NOT EXISTS student(" \
             "name VARCHAR(255) NOT NULL," \
             "nrstud INT NOT NULL" \
             ");"
cursorObject.execute(nowatabela)
print("Nowa tabela student została utworzona")
sqlins = "INSERT INTO student(name,nrstud) VALUES(%s,%s)"
val = ("Leon",63454)
cursorObject.execute(sqlins,val)
db.commit()
print(f"{cursorObject.rowcount} rekordów osadzono")
db.close()
