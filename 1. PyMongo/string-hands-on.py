import re

# text1 = "13/09/2021"
#
# if re.match(r'\d+/\d+/\d+', text1):
#     print("yes")
# else:
#     print("no")

text2 = "Today is 09/13/2021 python started on 3/13/2021"

regex = re.compile(r'\d+/\d+/\d+')            # returns a list

print(regex.findall(text2))

n = regex.match("09/13/2021")                 # returns a group
print(n.group(0))
