#!/usr/bin/env python3
"""
Example usage of The Golden Square Testing Project modules.

This script demonstrates how to use the various utilities and classes
provided by this project.
"""

from lib.fizzbuzz import fizzbuzz
from lib.greet import greet
from lib.counter import Counter
from lib.string_builder import StringBuilder
from lib.gratitudes import Gratitudes
from lib.password_checker import PasswordChecker
from lib.make_snippet import make_snippet


def main():
    """Demonstrate usage of all modules in the project."""
    
    print("🌟 Welcome to The Golden Square Testing Project Examples! 🌟\n")
    
    # FizzBuzz demonstration
    print("📊 FizzBuzz Demo:")
    for i in range(1, 16):
        result = fizzbuzz(i)
        print(f"  {i} -> {result}")
    print()
    
    # Greeting demonstration
    print("👋 Greeting Demo:")
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(f"  {greet(name)}")
    print()
    
    # Counter demonstration
    print("🔢 Counter Demo:")
    counter = Counter()
    print(f"  Initial: {counter.report()}")
    counter.add(5)
    print(f"  After adding 5: {counter.report()}")
    counter.add(10)
    print(f"  After adding 10: {counter.report()}")
    print()
    
    # StringBuilder demonstration
    print("🔤 StringBuilder Demo:")
    builder = StringBuilder()
    builder.add("Hello")
    builder.add(", ")
    builder.add("World")
    builder.add("!")
    print(f"  Built string: '{builder.output()}'")
    print(f"  String length: {builder.size()}")
    print()
    
    # Gratitudes demonstration
    print("🙏 Gratitudes Demo:")
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("health")
    gratitudes.add("technology")
    print(f"  {gratitudes.format()}")
    print()
    
    # Password Checker demonstration
    print("🔒 Password Checker Demo:")
    checker = PasswordChecker()
    test_passwords = ["short", "this_is_a_long_password", "medium123"]
    
    for password in test_passwords:
        try:
            result = checker.check(password)
            print(f"  '{password}' -> Valid! ✅")
        except Exception as e:
            print(f"  '{password}' -> {e} ❌")
    print()
    
    # Make Snippet demonstration
    print("✂️ Make Snippet Demo:")
    texts = [
        "Short text",
        "This is a medium length text example",
        "This is a very long text that should be truncated by the make snippet function"
    ]
    
    for text in texts:
        snippet = make_snippet(text)
        print(f"  Original: '{text}'")
        print(f"  Snippet:  '{snippet}'")
        print()
    
    print("🎉 Thanks for exploring The Golden Square Testing Project! 🎉")
    print("💡 Run 'python -m pytest tests/ -v' to see all tests in action!")


if __name__ == "__main__":
    main()