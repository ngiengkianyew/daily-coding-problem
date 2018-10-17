def generate_valid_ips(string, curr, all_ips):
    if len(curr) > 4 or (len(curr) < 4 and not string):
        return
    elif len(curr) == 4 and not string:
        all_ips.add(".".join(curr))
        return

    def recurse(index):
        generate_valid_ips(string[index:], curr + [string[0:index]], all_ips)

    recurse(1)
    first = int(string[0])
    if first and len(string) > 1:
        recurse(2)
        if len(string) > 2 and first < 3:
            recurse(3)


def generate_valid_ip_helper(string):
    all_ips = set()
    generate_valid_ips(string, list(), all_ips)
    return all_ips


# Tests
assert generate_valid_ip_helper("2542540123") == \
    {'254.25.40.123', '254.254.0.123'}
assert generate_valid_ip_helper("0000") == \
    {'0.0.0.0'}
assert generate_valid_ip_helper("255255255255") == \
    {'255.255.255.255'}
assert generate_valid_ip_helper("100100110") == \
    {'100.10.0.110', '10.0.100.110', '100.100.11.0', '100.100.1.10'}
