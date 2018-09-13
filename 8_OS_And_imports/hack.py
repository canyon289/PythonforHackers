"""
Python can tell the underlying shell to run commands. Handy when for replacing
bash scripts or calling tools in other languages

Brutespray examples
https://github.com/x90skysn3k/brutespray/blob/master/brutespray.py#L239

"""
# Other code can be brought in using the import statement
# Python has a really full featured built in library
import subprocess


PROTOCOLS = {"postgressql":"sql",
             "pop3": "email"}


PEOPLE_PROTOCOL = [["canyon289", "postgressql"],
                   ["Rtzq0", "pop3"]]


def pwn(people_protocol):
    """Actually hack people"""
    for person, protocol in people_protocol:
        try:
            command_to_run = "Hacking {0} with {1}".format(person, PROTOCOLS[protocol])
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


pwn(PEOPLE_PROTOCOL)
