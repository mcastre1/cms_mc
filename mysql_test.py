import mysql.connector as mysql

cnx = mysql.connect(user='mcastre1', password='Mc255587!', host='mysql.migcas21.dreamhosters.com', database='cms_mark_db')
cursor = cnx.cursor()

query = ("SELECT * FROM Cars")

cursor.execute(query)

for (RO, Make, Model, Year) in cursor:
    print(f"{RO}, {Make}, {Model}, {Year}")

cursor.close()
cnx.close()

print(f"Connected to: {cnx.get_server_info()}")