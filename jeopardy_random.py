import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("select cat.name, clu.text from category as cat, clue as clu where clu.category = cat.id order by random() limit 1")
results = cursor.fetchall()

print "Random categories:\n"
for ret in results:
    print 'Category: ' + ret[0]
    print 'Answer: ' + ret[1]

connection.close()
