#!/usr/bin/python
"""
A simplified version showing the difference

Try running the python file directly from the terminal
run "python simplified_example.py" from bash


Then start Python in its interactive REPL
run "import simplified_example" in python

And see what happens
"""
import argparse

parser = argparse.ArgumentParser(description="A sample Command Line Interface")
parser.add_argument('-u', '--username', help="Username of person to hack", required=True, default="Steve")
parser.add_argument('-p', '--password', help="Passwords to try", required=False)

# Set nargs to take a list of protocols
parser.add_argument('-pr', '--protocols', nargs='+', help="Protocols to try", required=False)

args = parser.parse_args()


if __name__ == "__main__":
    print(args.username)

    if args.password:
        print(args.password)
    else:
        print("No password provided")

    print(args.protocols)
