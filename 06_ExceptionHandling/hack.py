"""
If else, elseif are supported, space delimited like the rest of python

Brutespray examples
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L161
"""
protocols = {"postgressql":"sql",
             "pop3": "email"}


# Trying a get a protocol that does exist
print(protocols["pop3"])

# Trying to get a protocol that doesn't exist
# This raises what's called an exception
# Comment this line out to see how the rest of the code works
print(protocols["telnet"])


# This can be managed through try except
try:
    print(protocols["telnet"])
except KeyError:
    print("Telnet is not an option")


# In conjunction with the rest of the program

people_protocol = [["canyon289", "postgressql"],
                   ["Rtzq0", "pop3"],
                   ["Rtzq0", "telnet"]]

for person, protocol in people_protocol:
    try:
        print("Hacking {0} with {1}".format(person, protocols[protocol]))
    except KeyError:
        print("Protocol {} is not an option. Failed hack on {}".format(protocol, person))
