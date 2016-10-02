import os

import config

def join_path(*argc):
    """Join any number of path parts to correct path."""
    from operator import add
    return os.path.abspath(reduce(
        add,
        map(os.path.expanduser, argc),
        ""
    ))

def get_state_file():
    return join_path(config.DIRNAME, config.STATEFILE)


def ask(text, default=None):
    """Ask user a question in standard style."""

    while True:
        print("{text} [{0}/{1}]".format(
            "Y" if default == True else "y",
            "N" if default == False else "n",
            text=text
        ))
        s = raw_input()
        if s in ["Y", "y"]:
            return True
        elif s in ["N", "n"]:
            return False
        elif s == "" and default in [True, False]:
            return default


def run_in_dotfiles(command):
    """Run a command in dotfiles repo."""

    print(command)
    workdir = os.getcwd()
    os.chdir(os.path.expanduser(config.DIRNAME))
    val = os.system(command)
    os.chdir(workdir)
    if val != 0:
        raise Exception("return value of '{0}' is non-zero: {1}".format(command, val))


