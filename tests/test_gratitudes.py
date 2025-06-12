from lib.gratitudes import *

def test_initial_gratitudes_list_is_empty():
    gratitude = Gratitudes()
    assert gratitude.gratitudes == []

def test_add_single_gratitude():
    gratitude = Gratitudes()
    gratitude.add("my family")
    assert gratitude.gratitudes == ["my family"]