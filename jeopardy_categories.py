import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT name,game FROM category LIMIT 10")
results = cursor.fetchall()

print "Example categories:\n"
for category in results:
    print category[0] + '(game #' + str(category[1]) + ')'

connection.close()
