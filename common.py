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
