import sqlite3
from urllib import request

connection = sqlite3.connect("recipes.db")
cursor = connection.cursor()

cursor.execute('select name, url from recipes')
rows = cursor.fetchall()

print('\033[92m')

for name, url in rows:
    print("%s %s" % (name, url))
    recipe_html = request.urlopen(url).read().decode()
    cursor.execute('update recipes set raw_html = ? where name = ? ', (recipe_html, name))
    print(recipe_html)

connection.commit()
connection.close()  