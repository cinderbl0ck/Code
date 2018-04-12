import re
import urllib.request
import sys
from html.parser import HTMLParser
from pprint import pprint
import sqlite3

webpage_url = "http://pinchmysalt.com/recipe-list/"

class RecipeLinkHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.recipe_list = {}

    def handle_starttag(self,tag,attributes):
        if len(attributes) < 2:
            return
        if attributes[0][0] != 'title':
            return
        if attributes[1][0] != 'href':
            return
        if tag != 'a':
            return
        
        recipe_name = attributes[0][1]
        recipe_url = attributes[1][1]
        self.recipe_list[recipe_name] = recipe_url

    def print(self):
        pprint(self.recipe_list)

    def get_recipelist(self):
        return self.recipe_list

recipe_list_html = urllib.request.urlopen(webpage_url).read().decode()
parser = RecipeLinkHTMLParser()
parser.feed(recipe_list_html)
recipe_list_dict = parser.get_recipelist()

sanitary_recipe_list_dict = {}
for key, value in recipe_list_dict.items(): #.items needed in order to for loop over a dictionary
    if re.match(r'^ ?http',key): #skip recipe names that are http urls
        continue
    sanitary_recipe_list_dict[key.strip()] = re.sub(r'^\.\.','http://pinchmysalt.com', value) #substitute key starting with ".." with domain url and .strip removes extra spaces from end value

connection = sqlite3.connect("recipes.db")
cursor = connection.cursor()

for key, value in sanitary_recipe_list_dict.items():
    cursor.execute('insert into recipes (name, url) values ("%s", "%s")' % (key,value))
connection.commit()
connection.close()