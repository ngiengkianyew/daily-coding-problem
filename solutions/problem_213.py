def generate_valid_ips(string, curr, all_ips):
    if len(curr) == 4 and not string:
        all_ips.add(".".join(curr))
        return
    elif not string:
        return

    def recurse(index):
        generate_valid_ips(string[index:], curr + [string[0:index]], all_ips)

    recurse(1)
    first = int(string[0])
    if first:
        if len(string) > 1 and first > 0:
            recurse(2)
            if len(string) > 2 and first > 0 and first < 3:
                recurse(3)


def generate_valid_ip_helper(string):
    all_ips = set()
    generate_valid_ips(string, list(), all_ips)
    return all_ips


# Tests
assert not generate_valid_ip_helper(
    "2542540123") - set(['254.25.40.123', '254.254.0.123'])
assert not generate_valid_ip_helper(
    "0000") - set(['0.0.0.0'])
assert not generate_valid_ip_helper(
    "255255255255") - set(['255.255.255.255'])
