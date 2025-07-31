"""
The Golden Square Testing Project - Core Library

This package contains utility classes and functions demonstrating
test-driven development principles and best practices.
"""

from .fizzbuzz import fizzbuzz
from .greet import greet
from .counter import Counter
from .string_builder import StringBuilder
from .gratitudes import Gratitudes
from .password_checker import PasswordChecker
from .make_snippet import make_snippet

__version__ = "1.0.0"
__author__ = "Suhail Khan"

__all__ = [
    "fizzbuzz",
    "greet", 
    "Counter",
    "StringBuilder",
    "Gratitudes",
    "PasswordChecker",
    "make_snippet",
]