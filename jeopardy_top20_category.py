import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("select count(name), name from category group by name order by count(name) desc limit 20;")
results = cursor.fetchall()
for ret in results:
    print str(ret[0]) + ' ' + ret[1]

connection.close()
