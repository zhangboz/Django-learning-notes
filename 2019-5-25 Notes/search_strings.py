import re
patterns = ["term1","term2"]

text = 'This is a string with term1, not not the other!'

match =  re.search("term1",text)
print(match.start(),match.end())
