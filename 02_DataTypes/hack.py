"""
Python has many data types but the most widely used are

1. Strings
2. Lists
3. Dictionaries
4. Int/Float
5. None
6. Bool

EVERYTHING in Python is an object. If you don't know what this means
don't worry.

Brutespray examples
Dictionaries
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L130

Lists
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L338

Booleans
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L300

Strings
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L273

Int/Float
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L288
"""

# Lists are ordered and values are accessed by index
people = ["Steve", "Alice"]

# Strings are great things to print
print("Hacking " + people[0])
print("Hacking " + people[1])

# Dictionary are key value pairs useful for mapping one thing to another
protocols = {"postgressql": "sql",
             "pop3": "email"}

print("Hacking " + people[0] + "'s " + protocols["pop3"])
