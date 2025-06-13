from lib.present import Present
import pytest

"""when we wrap an item we get it
back by unwrapping"""

def test_wrap_and_the_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

"""is we unwrap before wrapping we
get an error message"""

def test_unwrap_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."
