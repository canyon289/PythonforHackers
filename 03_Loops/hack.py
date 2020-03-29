"""
Python supports for and while loops. Python is whitespace delimited
so code blocks are separated by spaces or tabs. Whatever you pick you have to stay consistent


Brutespray examples

For Loop
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L209
"""

people = ["Steve", "Alice"]

# Iteration in python is as easy as saying for thing in iterable
# Lists are one of many objects that support iterables
for person in people:
    print("Hacking " + person)

# Python supports variable unpacking in line with lists
protocols = {"postgressql": "sql",
             "pop3": "email"}

people_protocol = [["Steve", "postgressql"], ["Alice", "pop3"]]

for person, protocol in people_protocol:
    print("Hacking " + person + " with " + protocol)


# Advanced - List Comprehensions
# Just another way of doing the same thing above
print(["Hacking " + person + " with " + protocol for person, protocol in people_protocol])

