from lib.high_value import *

def test_get_highest_first_value_higher():
    hv = HighValue(10, 5)
    assert hv.get_highest() == "First value is higher"

def test_get_highest_second_value_higher():
    hv = HighValue(3, 8)
    assert hv.get_highest() == "Second value is higher"

def test_get_highest_values_equal():
    hv = HighValue(7, 7)
    assert hv.get_highest() == "Values are equal"

def test_add_to_first_value():
    hv = HighValue(5, 10)
    hv.add(3, "first")
    assert hv.value_first == 8
    assert hv.value_second == 10

def test_add_to_second_value():
    hv = HighValue(5, 10)
    hv.add(4, "second")
    assert hv.value_first == 5
    assert hv.value_second == 14

def test_add_invalid_selection_does_not_change_values():
    hv = HighValue(2, 3)
    hv.add(5, "unknown")
    assert hv.value_first == 2
    assert hv.value_second == 3
