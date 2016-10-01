#!/usr/bin/python2

from __future__ import print_function

import datetime
import os
import os.path
import sys

SAVEDIR = "dotfiles/"

def ask(text, default=None):
    """
    Ask user a question in standard style.
    """

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


def join_path(*argc):
    from operator import add
    return os.path.abspath(reduce(add, argc, ""))


def commit_changes(text=None):
    #TODO
    text = text or datetime.datetime.now().strftime("%c")
    os.system("git commit -am \"{0}\"".format(text))
    os.system("git push origin master")
    print("Commited changes with message '{0}'.".format(text))


def save_file(filename, yes=False):
    if yes or ask("Save {0}?".format(filename)):
        try:
            from_file = open(filename, "r")
            to_name = join_path(SAVEDIR, os.path.basename(filename))
            to_file = open(to_name, "w")
            to_file.write(from_file.read())
            os.system("git add {0}".format(to_file))
            print("Saved {0} to {1}".format(filename, to_name))
        except Exception as e:
            print("File {0} didn't save: {1}".format(filename, e))
        finally:
            from_file.close()
            to_file.close()


def save_files(filenames, text=None, yes=False):
    for f in filenames:
        save_file(f, yes)
    commit_changes(text)

save_files(sys.argv[1:])
