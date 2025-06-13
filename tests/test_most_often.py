from lib.most_often import *

def test_add_item_to_list():
    most_often = MostOften(["Apple", "Banana", "Cherries", "Apple"])
    most_often.add_new("Pear")
    assert most_often.starting_list == ["Apple", "Banana", "Cherries", "Apple", "Pear"]
    
def test_most_often():
    most_often = MostOften(["Apple", "Banana", "Cherries", "Apple"])
    assert most_often.get_most_often() == "Apple"

def test_for_a_tie():
    most_often = MostOften(["Apple", "Banana", "Cherries", "Apple", "Banana"])
    assert most_often.get_most_often() == "no clear winner"

def test_for_an_empty_list():
    most_often = MostOften([])
    assert most_often.starting_list == []