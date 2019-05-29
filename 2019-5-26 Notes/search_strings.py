################# Notes:

import re

################# 1. re.search(keyword, string)
patterns = ["term1","term2"]
text = 'This is a string with term1, not not the other!'
for pattern in patterns:
    print("im searching for "+ pattern)
    if re.search(pattern,text):
        print("match")
    else:
        print("nomatch")
### The "re.search(keyword, string)" method returns a match object, object returns true if keyword is in the string.


################# 2. The match object
match =  re.search("term1",text)
print(match.start(),match.end()) ##obj.start() and obj.end() are built in functions in re.match obj.

################# 3. re.split(split_keyword, string)
split_keyword = '@'
email = 'user@gmail.com'
print(re.split(split_keyword, email)) ## gives a list of strings [str1, str2]

################# 4. re.findall
print(re.findall('match', 'test phrase match in match middle')) ## gives a list of all occurances of the keyword

################# 5. string search methods. *+?
def multi_re_find(patternss, phrase):
    for pat in patternss:
        print(phrase)
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
test_pattern = ['sd*'] ######## : find the pattern with an s followed by 0 or more d.
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd+'] ######## : find the pattern with an s followed by 1 or more d.
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd?'] ######## : find the pattern with an s followed by 0 or 1 d.
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd{3}'] ######## : find the pattern with an s followed by 3 d.
multi_re_find(test_pattern, test_phrase)

test_pattern = ['sd{1,3}'] ######## : find the pattern with an s followed by 1 or 3 d.
multi_re_find(test_pattern, test_phrase)

test_pattern = ['s[sd]+'] ######## : find the pattern with an s followed by 1 or more s, or s followed by 1 or more d.
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
test_pattern = ['[^!.?]'] ######## : find the pattern of anything followed by a letter that is not (!.?).
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
test_pattern = ['[^!.?]+'] ######## : find the pattern of anything followed by letter that is not (!.?), the + means one or more of anything are acceptable. 
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
test_pattern = ['[a-z]+'] ######## : find all lower case characters. same for upper ['[A-Z]+']
multi_re_find(test_pattern, test_phrase) 

test_phrase = "This is a string with numbers 123123 and symbol #hashtag"
test_pattern = [r'\d+'] ######## : search for digits
multi_re_find(test_pattern, test_phrase) 

test_phrase = "This is a string with numbers 123123 and symbol #hashtag"
test_pattern = [r'\D+'] ######## : search for non-digits
multi_re_find(test_pattern, test_phrase) 

test_phrase = "This is a string with numbers 123123 and symbol #hashtag"
test_pattern = [r'\s+'] ######## : search for sequence of white space
multi_re_find(test_pattern, test_phrase) 

test_phrase = "This is a string with numbers 123123 and symbol #hashtag"
test_pattern = [r'\S+'] ######## : search for non-white space
multi_re_find(test_pattern, test_phrase) 

test_phrase = "This is a string with numbers 123123 and symbol #hashtag"
test_pattern = [r'\w+'] ######## : search for all alpha and numeric characters
multi_re_find(test_pattern, test_phrase) 

test_phrase = "This is a string with numbers 123123 and symbol #hashtag"
test_pattern = [r'\W+'] ######## : search for all non-(alpha and numeric) characters
multi_re_find(test_pattern, test_phrase) 