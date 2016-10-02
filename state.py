"""Load and save state."""
import pickle

import common
import config

def open_file(mode="rw"):
    """
    Decorator for opening specified or default file.
    """
    def wrapper(func):
        def wrapped(*args, **kwargs):
            args = list(args)
            args.append(open(kwargs.get("f", common.get_state_file()), mode))
            try:
                del(kwargs["f"])
            finally:
                return func(*args, **kwargs)
        return wrapped
    return wrapper


@open_file("r")
def load_state(f):
    return pickle.load(f)

@open_file("w")
def save_state(state, f):
    pickle.dump(state, f)
