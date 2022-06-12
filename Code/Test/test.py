from sample import calculate_sum, find_divisor, check_perfect_number
import pytest

# Unit test (Automation)

def test1_calculate_sum():
    test_data = [1,2,3,4]
    expected_data = 10
    actual_data = calculate_sum(test_data)
    assert expected_data == actual_data

def test2_calculate_sum():
    test_data = [1]
    expected_data = 1
    actual_data = calculate_sum(test_data)
    assert expected_data == actual_data

def test3_calculate_sum():
    test_data = []
    expected_data = 0
    actual_data = calculate_sum(test_data)
    assert expected_data == actual_data

def test4_calculate_sum():
    test_data = [-5, 2, 2, 1]
    expected_data = 0
    actual_data = calculate_sum(test_data)
    assert expected_data == actual_data

def test1_find_divisor():
    test_data = 9
    expected_data = [9, 3, 1]
    actual_data = find_divisor(test_data)
    assert expected_data == actual_data

def test2_find_divisor():
    test_data = 17
    expected_data = [17, 1]
    actual_data = find_divisor(test_data)
    assert expected_data == actual_data

def test3_find_divisor():
    test_data = 1
    expected_data = [1]
    actual_data = find_divisor(test_data)
    assert expected_data == actual_data

def test4_find_divisor():
    test_data = 0
    expected_data = []
    actual_data = find_divisor(test_data)
    assert expected_data == actual_data

def test1_check_perfect_number():
    test_data = 6
    expected_data = True
    actual_data = check_perfect_number(test_data)
    assert expected_data == actual_data

def test2_check_perfect_number():
    test_data = 17
    expected_data = False
    actual_data = check_perfect_number(test_data)
    assert expected_data == actual_data

def test3_check_perfect_number():
    test_data = 1
    expected_data = False
    actual_data = check_perfect_number(test_data)
    assert expected_data == actual_data

def test4_check_perfect_number():
    test_data = 0
    expected_data = False
    actual_data = check_perfect_number(test_data)
    assert expected_data == actual_data