import os
import string
os.chdir("D:\\CS")
file = open("hapaxassignment.txt", "r")
text = file.read()
lowertext = text.lower()

exclist = string.punctuation + string.digits
table_ = str.maketrans('', '', exclist)
newtext = lowertext.translate(table_)

words = newtext.split()


frequency = []
for word in words:
    frequency.append(words.count(word))
    if words.count(word) == 1:
        print(word)