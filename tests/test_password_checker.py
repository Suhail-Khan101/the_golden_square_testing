from lib.password_checker import *
import pytest

def test_valid_password_returns_true():
    checker = PasswordChecker()
    result = checker.check("secure123")
    assert result is True

def test_short_password_raises_exception():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("short")
    assert str(e.value) == "Invalid password, must be 8+ characters."
