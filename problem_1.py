def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if not isinstance(number, int):
        raise ValueError("Please provide integer as input value")

    if number < 0:
        raise ValueError("Function defined on positive numbers")

    begin = 1
    end = number

    while True:
        middle = begin + (end - begin) // 2
        r = middle ** 2

        if begin == end or end - begin == 1:
            return begin

        if r == number:
            return middle

        if r > number:
            end = middle
        else:
            begin = middle


print ("Pass" if  (3 == sqrt(9)) else "Fail")  # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")  # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")  # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")   # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")  # Pass

# Edge cases
try:
    sqrt(-1)
except ValueError as e:
    print(e)  # Should print error

try:
    sqrt('')
except ValueError as e:
    print(e) # Should print value
