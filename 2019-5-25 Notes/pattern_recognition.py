import re
patterns = ["term1","term2"]

text = 'This is a string with term1, not not the other!'
for item in patterns:
    print("I'm searching for: "+item)
    if re.search(item,text):
        print("MATCH!")
    else:
        print("NO MATCH")