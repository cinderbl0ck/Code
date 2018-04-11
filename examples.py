class WebSearchArguments:
    def __init__(self, arguments_array):
        self.search = arguments_array[1]
        self.url = arguments_array[2]

arguments = WebSearchArguments(sys.argv)

print(arguments.url)
print(arguments.search)

'''def count_ts(text):
    count_ts counts the number of times the letter "t" occurs in text, must be a bytearray
    count = 0
    for letter in text:
        if letter == 116:
            count = count + 1 
    return count 

def count_fuck(text):
    count_fuck counts the number of times the letters "f" "u" "c" "k" are present in text, bytearrayformat 
    count117 = 0
    count107 = 0
    count102 = 0
    count99 = 0
    for letter in text:
        if letter == 117: count117 += 1
        if letter == 107: count107 += 1
        if letter == 102: count102 += 1
        if letter == 99: count99 += 1
    return min(count117, count107, count102, count99)'''

def count_pumpkins(text):
    pumpkins = 0
    for offset in re.finditer(arguments.search, text.decode()):
        pumpkins += 1
    return pumpkins
