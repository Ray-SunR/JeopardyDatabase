import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT clu.text, clu.answer, cat.name FROM clue as clu, category as cat where clu.value = 800 and clu.category = cat.id LIMIT 10")
results = cursor.fetchall()

print "\nExample clues:\n"
for clue in results:
    text, answer, category = clue
    print 'Cateogry: ' + category
    print 'Question: ' + text
    print 'Answer: ' + answer
    print '==='

connection.close()
