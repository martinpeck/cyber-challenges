import re

# string to search
ex = "hello1goodbye2seeya3"

# compile the regular expression
rx = re.compile("\d")

# find all of the matches in ex using the regular expression
matches = rx.findall(ex)

# print all of the matches as a list ['1', '2', '3']
print(matches)
