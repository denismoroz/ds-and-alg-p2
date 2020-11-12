
def merge_sort(input_list):

    if len(input_list) <= 1:
        return input_list

    middle = len(input_list) // 2

    left = merge_sort(input_list[:middle])
    right = merge_sort(input_list[middle:])

    return _merge(left, right)


def _merge(left, right):
    result = []

    while left and right:
        l = left[0]
        r = right[0]

        if l < r:
            result.append(l)
            left.pop(0)
        else:
            result.append(r)
            right.pop(0)

    return result + left + right


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) <= 1:
        return [-1, -1]

    input_list = merge_sort(input_list)

    first = ''
    second = ''

    for i in range(len(input_list) - 1, -1, -1):
        if i % 2 == 0:
            second += str(input_list[i])
        else:
            first += str(input_list[i])

    return [int(first), int(second)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])  # Pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)  # Pass
test_function([[1, 1, 1, 3, 5, 6], [631, 511]])  # Pass

# Edge cases
test_function([[], [-1, -1]])  # Pass
test_function([[0], [-1, -1]])  # Pass
test_function([[0, 0], [0, 0]])  # Pass
