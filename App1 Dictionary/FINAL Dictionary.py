
#This app is a dictionary that takes a user input and returns a
#definition output
#it also has a matching system accounting for spelling errors



import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
#automatically loads json contents into a dict object!

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Y/N \n" % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "Sorry we don't have anything for you."
    else:
        return "Word does not exist."

word = str(input("enter a word "))
output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

# print(type(data))
# # print(data[rain]) returns <class 'dict'>


print(SequenceMatcher(None, "rainn","rain").ratio())
