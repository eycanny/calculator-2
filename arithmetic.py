"""Functions for common math operations."""

def add(nums):
    """Return the sum of all input integers."""
    total = 0
    i = 1

    while i < len(nums):
        num = float(nums[i])
        total += num
        i += 1

    return total


def subtract(nums):
    """Return the sum of subsequent numbers from the first number."""
    # test list = ['-', '100', '50', '20']
    first_number = float(nums[1])
    sum_of_subsequent_numbers = 0
    i = 2

    while i < len(nums):
        num = float(nums[i])
        sum_of_subsequent_numbers += num
        i += 1

    total = first_number - sum_of_subsequent_numbers

    return total


def multiply(nums):
    """Multiply the all inputs together."""
    #test list: ['*', '2', '2', '3', '4'] -> output: 48
    total = float(nums[1])
    i = 2

    while i < len(nums):
        total = total * float(nums[i])
        i +=1

    return total


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of the input."""

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
