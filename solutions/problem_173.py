def is_dict(var):
    return str(type(var)) == "<class 'dict'>"


def flatten_helper(d, flat_d, path):
    if not is_dict(d):
        flat_d[path] = d
        return

    for key in d:
        new_keypath = "{}.{}".format(path, key) if path else key
        flatten_helper(d[key], flat_d, new_keypath)


def flatten(d):
    flat_d = dict()
    flatten_helper(d, flat_d, "")
    return flat_d


# Tests

d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

assert flatten(d) == {
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
