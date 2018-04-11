import sys
from urllib import request

class CurlArguments:
    def __init__(self, arguments_array):
        self.url = arguments_array[1]

arguments = CurlArguments(sys.argv)

html = request.urlopen(arguments.url).read()
print(html.decode())