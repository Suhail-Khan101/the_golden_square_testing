#!/usr/bin/env python3
"""
Setup script for The Golden Square Testing Project.

This script helps users get started with the project quickly.
"""

import subprocess
import sys
import os


def run_command(command, description):
    """Run a command and print the result."""
    print(f"📋 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully!")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} failed!")
            print(f"   Error: {result.stderr.strip()}")
        print()
        return result.returncode == 0
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        print()
        return False


def main():
    """Setup the project environment."""
    print("🌟 Welcome to The Golden Square Testing Project Setup! 🌟\n")
    
    # Check Python version
    print(f"🐍 Python version: {sys.version}")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        sys.exit(1)
    print("✅ Python version is compatible!\n")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("❌ Failed to install dependencies. Please install manually.")
        sys.exit(1)
    
    # Run tests
    if not run_command("python -m pytest tests/ -v", "Running tests"):
        print("❌ Some tests failed. Please check the output above.")
        sys.exit(1)
    
    # Run examples
    if not run_command("python examples.py", "Running examples"):
        print("❌ Examples failed to run. Please check the output above.")
        sys.exit(1)
    
    print("🎉 Setup completed successfully!")
    print("\n📚 What you can do now:")
    print("   • Run tests: python -m pytest tests/ -v")
    print("   • See examples: python examples.py")
    print("   • Import modules: from lib import fizzbuzz, greet, Counter")
    print("   • Read documentation: cat README.md")
    print("\n💡 Happy coding with The Golden Square methodology! 💡")


if __name__ == "__main__":
    main()