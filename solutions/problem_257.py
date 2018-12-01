from heapq import heappush as hp


def get_sort_range(arr):
    if arr == sorted(arr):
        return ()

    options = list()
    for sort_start in range(len(arr) - 1):
        for sort_end in range(1, len(arr) + 1):
            a1 = arr[:sort_start]
            a2 = arr[sort_start:sort_end]
            a3 = arr[sort_end:]

            new_arr = a1 + sorted(a2) + a3
            if new_arr == sorted(new_arr):
                # options.append((sort_start, sort_end - 1))
                hp(options, (sort_end - sort_start, (sort_start, sort_end - 1)))

    return options[0][1]


# Test
assert get_sort_range([3, 5, 6, 7, 9]) == ()
assert get_sort_range([3, 7, 5, 6, 9]) == (1, 3)
assert get_sort_range([5, 4, 3, 2, 1]) == (0, 4)
