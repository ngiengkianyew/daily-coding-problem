def find_element(arr, element, start, end):

    if start == end:
        return

    mid = start + ((end - start) // 2)

    if arr[mid] == element:
        return mid
    elif arr[mid] > element:
        if arr[start] >= element:
            return find_element(arr, element, start, mid)
        else:
            return find_element(arr, element, mid, end)
    elif arr[mid] < element:
        if arr[start] <= element:
            return find_element(arr, element, start, mid)
        else:
            return find_element(arr, element, mid, end)


def find_element_main(arr, element):
    element_pos = find_element(arr, element, 0, len(arr))
    return element_pos


assert find_element_main([13, 18, 25, 2, 8, 10], 2) == 3
assert find_element_main([13, 18, 25, 2, 8, 10], 8) == 4
assert find_element_main([25, 2, 8, 10, 13, 18], 8) == 2
assert find_element_main([8, 10, 13, 18, 25, 2], 8) == 0
