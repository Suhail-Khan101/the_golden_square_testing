from lib.present import Present
import pytest

"""when we wrap an item we get it
back by unwrapping"""

def test_wrap_and_the_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

"""if we unwrap before wrapping we
get an error message"""

def test_unwrap_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

"""if we try to wrap an already wrapped present we
get an error message"""

def test_wrapping_already_wrapped_throws_error():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

"""if we try to wrap an already wrapped present, the
first wrapped value is unchanged"""

def test_wrapping_already_wrapped_preserves_values():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44
