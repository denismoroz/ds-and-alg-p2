def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return search(input_list, number, 0, len(input_list) -1)


def search(input_list, number, start, end):
    if end - start == 1 or start == end:
        if input_list[start] == number:
            return start
        if input_list[end] == number:
            return end

        return -1

    middle = start + (end - start) // 2

    # start, middle
    start_item = input_list[start]
    middle_item = input_list[middle]
    end_item = input_list[end]

    res = -1

    if start_item <= middle_item:
        if start_item <= number <= middle_item:
            return search(input_list, number, start, middle)
    else:
        res = search(input_list, number, start, middle)

    if res != -1:
        return res

    if middle_item <= end_item:
        if middle_item <= number <= end_item:
            return search(input_list, number, middle, end)
    else:
        res = search(input_list, number, middle, end)

    return res


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])