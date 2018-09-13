"""
Wrap up all our logic in a command line interface for easy use

Brutespray example
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L306
"""
import subprocess
import os
import argparse


PROTOCOLS = {"postgressql": "sql",
             "pop3": "email"}


# An example of OS dependent things are filepaths. Windows does it differently than Linux
# by using os.path.join we avoid cross platform problems
filepath = os.path.join("passwords", "passwords.txt")

# This opens the file in read mode
with open(filepath, 'r') as password_file:
    # A list comprehension to make things compact
    # rstrip just removes the \n (newline) character from the end of the string
    PASSWORDS = [line.rstrip() for line in password_file]

print(PASSWORDS)


def pwn(people, passwords, protocols):
    """Actually hack people

    Added passwords as an argument this time
    """
    # Extra for loop to try each password for each user, protocol pair
    for password in passwords:
        for person in people:
            for protocol in protocols:
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


parser = argparse.ArgumentParser(description="A sample Command Line Interface")
parser.add_argument('-u', '--username', nargs='+', help="Usernames of people to hack", required=True, default="canyon289")
parser.add_argument('-p', '--password', nargs='+', help="Passwords to try", required=False)
parser.add_argument('-pr', '--protocols', nargs='+', help="Protocols to try", required=False)

args = parser.parse_args()

"""
"Scripts" are usually things that are run directly e.g. python hack.py
Programs or libraries rae things that are usually imported
The problem is that when you import things in python it actually runs the codeo
So typically you should separate the "definitions" from the "actions"
In our example we want to separate the actual pwning from the instructions on how to pwn

Refer to the simplified example in this same directory
"""

if __name__ == "__main__":
    users_to_hack = args.username

    if args.password:
        passwords = args.password
    else:
        print("No password provided using default password list")
        passwords = PASSWORDS

    protocols = args.protocols
    pwn(users_to_hack, passwords, protocols)
