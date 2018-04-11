import re
import urllib.request
import sys
from html.parser import HTMLParser
from pprint import pprint

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

recipe_list_html = urllib.request.urlopen(webpage_url).read().decode()
parser = RecipeLinkHTMLParser()
parser.feed(recipe_list_html)
parser.print()




