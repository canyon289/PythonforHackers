"""
Loading things from files are very useful. In Brutespray password lists are defined
per protocol

Brutespray examples
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L155
https://github.com/x90skysn3k/brutespray/tree/master/wordlist
"""
import subprocess

# Yet another import. OS helps us abstract away the operating system which helps when you want to
# run your code on either multiple operating systems without problems
import os


PROTOCOLS = {"postgressql": "sql",
             "pop3": "email"}


PEOPLE_PROTOCOL = [["canyon289", "postgressql"],
                   ["Rtzq0", "pop3"]]


# An example of OS dependent things are filepaths. Windows does it differently than Linux
# by using os.path.join we avoid cross platform problems
filepath = os.path.join("passwords", "passwords.txt")

# This opens the file in read mode
with open(filepath, 'r') as password_file:
    # A list comprehension to make things compact
    # rstrip just removes the \n (newline) character from the end of the string
    PASSWORDS = [line.rstrip() for line in password_file]

print(PASSWORDS)


def pwn(people_protocol, passwords):
    """Actually hack people

    Added passwords as an argument this time
    """
    # Extra for loop to try each password for each user, protocol pair
    for password in passwords:
        for person, protocol in people_protocol:
            try:
                command_to_run = "Hacking {0} with {1} using {2}".format(person, PROTOCOLS[protocol], password)
                # This command is being run in the shell directly, not in Python!
                subprocess.run(['echo', "{}".format(command_to_run)])

            except KeyError:
                print("Protocol {} is not an option. Failed hack on {}".format(protocol, person))

    return


def print_targets(people_protocol):
    """Just print the names and protocols"""
    for hack_pair in people_protocol:
        print(hack_pair)
    return


pwn(PEOPLE_PROTOCOL, PASSWORDS)
