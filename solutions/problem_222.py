PATH_SEPARATOR = "/"


def shorten_path(path):
    stack = list()
    dirs = path.split(PATH_SEPARATOR)

    for dir_name in dirs:
        if dir_name == ".":
            continue
        elif dir_name == "..":
            stack.pop()
        else:
            stack.append(dir_name)

    spath = PATH_SEPARATOR.join(stack)
    return spath


# Tests
assert shorten_path("/usr/bin/../bin/./scripts/../") == "/usr/bin/"
