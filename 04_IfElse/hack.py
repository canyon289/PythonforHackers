"""
If else, elseif are supported, space delimited like the rest of python

Brutespray examples

If statement. They're basically everywhere in Brutespray
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L213
"""

protocols = {"postgressql":"sql",
             "pop3": "email"}

people_protocol = [["Steve", "postgressql"],
                   ["Alice", "pop3"],
                   ["Alice", "sql"]]

for person, protocol in people_protocol:
    # Equality is one type of conditional
    # Equal is denoted as ==
    # Single = is called an assignment operator for reference
    if person == "Alice":
        print("Hacking " + person + " with " + protocol + " even harder")
    else:
        print("Hacking " + person + " with " + protocol)


# And/Or statements can be used with conditionals as well
for person, protocol in people_protocol:
    if person == "Alice" and protocol == "pop3":
        print("Hacking " + person + " with " + protocol + " with phishing")

    elif person == "Alice" and protocol == "sql":
        print("Hacking " + person + " with " + protocol + " with sqlinjection")

    else:
        print("Hacking " + person + " with " + protocol)
