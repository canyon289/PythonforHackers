"""
If else, elseif are supported, space delimited like the rest of python

Brutespray examples
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L239
"""

# Variables in global scope are suggested to be capitalized by convention
PROTOCOLS = {"postgressql": "sql",
             "pop3": "email"}


PEOPLE_PROTOCOL = [["canyon289", "postgressql"],
                   ["Rtzq0", "pop3"],
                   ["Rtzq0", "sql"]]


def pwn(people_protocol):
    """Actually hack people"""
    for person, protocol in people_protocol:
        try:
            print("Hacking {0} with {1}".format(person, PROTOCOLS[protocol]))
        except KeyError:
            print("Protocol {} is not an option. Failed hack on {}".format(protocol, person))

    # Return statement is not needed if nothing is being returned but I like putting them in
    return


def print_targets(people_protocol):
    """Just print the names and protocols"""
    for hack_pair in people_protocol:
        print(hack_pair)
    return


print_targets(PEOPLE_PROTOCOL)
pwn(PEOPLE_PROTOCOL)
