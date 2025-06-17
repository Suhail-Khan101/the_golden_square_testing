from lib.fizzbuzz import *

"""Given a number not divisible by 3 or 5 (e.g. 1)
it returns that number"""

def test_given_non_3_5_divisible_returns_number():
    result = fizzbuzz(1)
    assert result == 1

"""Given a number divisible by 3
It returns Fizz"""

def test_given_3_divisible_returns_fizz():
    result = fizzbuzz(3)
    assert result == "Fizz"

"""Given a number divisible by 5
It returns Buzz"""

def test_given_3_divisible_returns_fizz():
    result = fizzbuzz(5)
    assert result == "Buzz"

"""Given a number divisible by 3 and 5
It returns FizzBuzz"""

def Test_given_3_and_5_divisible_returns_FizzBuzz():
    result = fizzbuzz(15)
    assert result == "FizzBuzz"






