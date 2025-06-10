from lib.report_length import *

def test_length_of_string():
    result = report_length("Sunshine")
    assert result == "This string was 8 characters long."
