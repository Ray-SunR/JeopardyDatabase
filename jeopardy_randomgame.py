import sqlite3
import random
connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()
cursor.execute("select max(game),min(game) from category")

maxmin = cursor.fetchall()
pick = random.randint(maxmin[0][1], maxmin[0][0])
cursor.execute("select round, name from category where game = " + str(pick))

results = cursor.fetchall()
print 'Categories for game #' + str(pick) + ':'
for ret in results:
    print str(ret[0]) + ' ' + str(ret[1])

connection.close()
