from lib.gratitudes import *

def test_initial_gratitudes_list_is_empty():
    gratitude = Gratitudes()
    assert gratitude.gratitudes == []

def test_add_single_gratitude():
    gratitude = Gratitudes()
    gratitude.add("my family")
    assert gratitude.gratitudes == ["my family"]

def test_add_multiple_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("my health")
    gratitude.add("my friends")
    gratitude.add("good food")
    assert gratitude.gratitudes == ["my health", "my friends", "good food"]

def test_format_single_gratitude():
    gratitude = Gratitudes()
    gratitude.add("sunshine")
    result = gratitude.format()
    assert result == "Be grateful for: sunshine"

def test_format_multiple_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("coffee")
    gratitude.add("books")
    gratitude.add("weekends")
    result = gratitude.format()
    assert result == "Be grateful for: coffee, books, weekends"

def test_format_with_no_gratitudes():
    gratitude = Gratitudes()
    result = gratitude.format()
    assert result == "Be grateful for: "