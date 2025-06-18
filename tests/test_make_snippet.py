from lib.make_snippet import *

# Design

# A function called make_snippet that takes a string as 
# an argument and returns the first five words and 
# then a '...' if there are more than that.

"""If given an empty string it returns an empty string"""

def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""

"""Given a string of four words
it returns the same string"""

def test_given_four_word_string_returns_same_string():
    result = make_snippet("one two three four")
    assert result == "one two three four"

"""Given a string of five words
it returns the same string"""

def test_given_five_word_string_returns_same_string():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

"""Given a string of six words
it returns the first five words and a ..."""

def test_given_six_words_returns_string_and_ellipsis():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."
