import abc
import pytest


def calculate_sum(xs):
    """Compute sum of an array

    Args:
        xs (list): array that need to compute

    Returns:
        float: sum of xs
    """
    result = 0
    for x in xs:
        result += x
    return result


def find_divisor(x):
    """Find all divisor of an integer

    Args:
        x (int)

    Returns:
        list: list of divisor
    """
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    divisors.reverse()
    return divisors


def check_perfect_number(x):
    """Check if a integer is perfect number. 
    Ex: 6 is a perfect number because its divisors are 1,2,3 and
    1 + 2 + 3 = 6

    6 = [1, 2, 3]

    Args:
        x (integer): the integer that need to check

    Returns:
        boolean: Checked result
    """
    if x == 0:
        return False
        
    if calculate_sum(find_divisor(x)) == 2*x:
        return True
    return False
    


