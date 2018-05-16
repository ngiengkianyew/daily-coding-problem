def partition_helper(mset, start, end, outer_sum, inner_sum):
    if start >= end:
        return False
    if outer_sum == inner_sum:
        return True

    return \
        partition_helper(mset, start + 1, end, outer_sum + mset[start],
                         inner_sum - mset[start]) or \
        partition_helper(mset, start, end - 1, outer_sum + mset[end],
                         inner_sum - mset[end])


def can_partition(mset):
    if not mset:
        return True

    if sum(mset) % 2 == 1:
        return False

    mset.sort()

    return partition_helper(mset, 0, len(mset) - 1, 0, sum(mset))


assert can_partition([15, 5, 20, 10, 35, 15, 10])
assert not can_partition([15, 5, 20, 10, 35])
assert can_partition([1, 2, 3, 4, 9, 1])
assert can_partition([1, 1, 1, 1, 1, 1, 6])
