#!/usr/bin/python2

from __future__ import print_function

import datetime
import os
import os.path

import config
import common
import state


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

    workdir = os.getcwd()
    os.chdir(os.path.expanduser(config.DIRNAME))
    val = os.system(command)
    os.chdir(workdir)
    if val != 0:
        raise Exception("return value of '{0}' is non-zero: {1}".format(command, val))


def commit_changes(text=None):
    """Commit changes to git repository."""
    text = text or datetime.datetime.now().strftime("%c")
    run_in_dotfiles("git commit -m \"{0}\"".format(text))
    run_in_dotfiles("git push origin master")
    print("Commited changes with message '{0}'.".format(text))


def save_file(filename, yes=False):
    """Save file in SAVEDIR."""
    if yes or ask("Save {0}?".format(filename, default=True)):
        try:
            # --> make name to save
            new_name = os.path.basename(filename)
            if new_name[0] == ".":
                new_name = new_name[1:]
            # <-- make name to save

            # --> check state
            st = state.load_state()
            if st.get(new_name) != filename:
                if not ask("File {0} was saved from a different place({1}). Replace?".format(
                    filename, st.get(new_name)
                ), default=False):
                    raise Exception("file has already been saved from another place")
            # <-- check state

            # --> copy file
            from_file = open(filename, "r")
            to_name = common.join_path(config.DIRNAME, new_name)
            to_file = open(to_name, "w")
            to_file.write(from_file.read())
            # <-- copy file
            
            # --> update state
            st[new_name] = filename
            state.save_state(st)
            # <-- update state

            # --> git stuff
            run_in_dotfiles("git add {0} {1}".format(to_name, common.get_state_file()))
            # --> git stuff

            print("Saved {0} to {1}".format(filename, to_name))
        except Exception as e:
            print("File {0} didn't save: {1}".format(filename, e))
        finally:
            try:
                from_file.close()
                to_file.close()
            except:
                pass


def save_files(filenames, text=None, yes=False):
    """Save some files and commit them."""
    for f in filenames:
        save_file(f, yes)
    commit_changes(text)

