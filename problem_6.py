def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not isinstance(ints, list):
        raise ValueError("Please provide a list as input parameter")

    min = None
    max = None

    for i in ints:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i

    return min, max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  # Pass
print("Pass" if ((1, 95) == get_min_max([2, 4, 1, 2, 95])) else "Fail")  # Pass
print("Pass" if ((-10, 12) == get_min_max([-1, -10, 12, 3, 9])) else "Fail")  # Pass

# Edge cases

try:
    get_min_max(None)
except ValueError as e:
    print(e) # Please, provide a list as input

print("Pass" if ((None, None) == get_min_max([])) else "Fail")  # Pass