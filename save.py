#!/usr/bin/python2

from __future__ import print_function

import datetime
import os
import os.path

import config
import common
import state



def commit_changes(text=None):
    """Commit changes to git repository."""
    text = text or datetime.datetime.now().strftime("%c")
    common.run_in_dotfiles("git commit -m \"{0}\"".format(text))
    common.run_in_dotfiles("git push origin master")
    print("Commited changes with message '{0}'.".format(text))


def save_file(filename, yes=False):
    """Save file in SAVEDIR."""
    if yes or common.ask("Save {0}?".format(filename, default=True)):
        try:
            # --> make name to save
            new_name = os.path.basename(filename)
            if new_name[0] == ".":
                new_name = new_name[1:]
            # <-- make name to save

            # --> check state
            st = state.load_state()
            if new_name in st and st[new_name] != filename:
                if not common.ask("File {0} was saved from a different place({1}). Replace?".format(
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
            common.run_in_dotfiles("git add {0} {1}".format(to_name, common.get_state_file()))
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

