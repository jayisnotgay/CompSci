# Number 2

import os
import string
os.chdir("D:\\CS")

file = open("hapaxassignment.txt", "r")
newfile = open("new_text1.txt", "w")

lines=file.read().split("\n")

number=1
for line in lines:
    newfile.write(str(number) +". "+line+"\n")
    number += 1

file.close()
newfile.close()

# Number 3
file = open("hapaxassignment.txt", "r")
text = file.read().lower()
exclist = string.punctuation + string.digits
table_ = str.maketrans('', '', exclist)
newtext = text.translate(table_)
words = newtext.split()
sum=0
for letters in words:
    sum += len(letters)

print(sum/len(words))

file.close()

# Number 4

file = open("miyagi.txt", "r")
text = file.read().split()
titles = ("Mr.","Ms.","Dr.","Jr.","Mrs.")
abbreviations = ("i.e.")
newtext = ""
print(text)
for word in text:
    if "?" not in word and "!" not in word:
        newtext+=(word + " ")
        if word not in titles and word not in abbreviations and "." in word[-1]:
            newtext+="\n"
    else:
        newtext+=(word+"\n")


print(newtext)
