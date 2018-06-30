# source - https://gist.github.com/kylebebak/ee67befc156831b3bbaa88fb197487b0

import time


def debounce(s):
    """
    Decorator ensures function that can only be called once every `s` seconds.
    """
    interval = s * (10**(-3))

    def decorate(f):
        current_time = None

        def wrapped(*args, **kwargs):
            nonlocal current_time
            start_time = time.time()
            if current_time is None or start_time - current_time >= interval:
                result = f(*args, **kwargs)
                current_time = time.time()
                return result
        return wrapped
    return decorate


@debounce(3000)
def add_nums(x, y):
    return x + y


assert add_nums(1, 1) == 2
time.sleep(1)
assert not add_nums(1, 2)
time.sleep(1)
assert not add_nums(1, 3)
time.sleep(1)
assert add_nums(1, 4) == 5
