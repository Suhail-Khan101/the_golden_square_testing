# The Golden Square Testing Project

A comprehensive Python project demonstrating test-driven development (TDD) principles and best practices. This project contains multiple utility classes and functions, each thoroughly tested to ensure reliability and correctness.

## 🚀 Features

This project includes the following modules:

### Core Utilities
- **FizzBuzz** (`lib/fizzbuzz.py`) - Classic FizzBuzz implementation
- **Greet** (`lib/greet.py`) - Simple greeting function
- **StringBuilder** (`lib/string_builder.py`) - String building utility class
- **Counter** (`lib/counter.py`) - Counting utility class
- **MakeSnippet** (`lib/make_snippet.py`) - Text snippet creation utility

### Advanced Features
- **Gratitudes** (`lib/gratitudes.py`) - Gratitude list manager
- **PasswordChecker** (`lib/password_checker.py`) - Password validation utility
- **HighValue** (`lib/high_value.py`) - Value comparison utility
- **CheckCodeword** (`lib/check_codeword.py`) - Codeword validation
- **Reminder** (`lib/reminder.py`) - Task reminder system
- **Present** (`lib/present.py`) - Gift wrapping simulation
- **MostOften** (`lib/most_often.py`) - Frequency analysis utility
- **ReportLength** (`lib/report_length.py`) - String length reporting

## 📋 Requirements

- Python 3.8 or higher
- pytest 8.4.0 or higher

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Suhail-Khan101/the_golden_square_testing.git
cd the_golden_square_testing
```

2. Quick setup (recommended):
```bash
python setup.py
```

3. Or install dependencies manually:
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

Run all tests:
```bash
python -m pytest tests/ -v
```

Run tests with coverage:
```bash
python -m pytest tests/ --cov=lib --cov-report=html
```

Run specific test file:
```bash
python -m pytest tests/test_fizzbuzz.py -v
```

## 💡 Usage Examples

### Quick Start
Run the setup script to get started immediately:
```bash
python setup.py
```

Or see all examples in action:
```bash
python examples.py
```

### Individual Module Usage

### FizzBuzz
```python
from lib.fizzbuzz import fizzbuzz

print(fizzbuzz(15))  # "FizzBuzz"
print(fizzbuzz(3))   # "Fizz"
print(fizzbuzz(5))   # "Buzz"
print(fizzbuzz(7))   # 7
```

### Counter
```python
from lib.counter import Counter

counter = Counter()
counter.add(5)
counter.add(3)
print(counter.report())  # "Counted to 8 so far."
```

### Gratitudes
```python
from lib.gratitudes import Gratitudes

gratitudes = Gratitudes()
gratitudes.add("family")
gratitudes.add("health")
print(gratitudes.format())  # "Be grateful for: family, health"
```

### StringBuilder
```python
from lib.string_builder import StringBuilder

builder = StringBuilder()
builder.add("Hello, ")
builder.add("World!")
print(builder.output())  # "Hello, World!"
print(builder.size())    # 13
```

### Password Checker
```python
from lib.password_checker import PasswordChecker

checker = PasswordChecker()
try:
    result = checker.check("password123")
    print("Password is valid!")
except Exception as e:
    print(f"Error: {e}")
```

## 🏗️ Project Structure

```
the_golden_square_testing/
├── lib/                    # Source code modules
│   ├── __init__.py
│   ├── fizzbuzz.py
│   ├── greet.py
│   ├── counter.py
│   ├── string_builder.py
│   ├── gratitudes.py
│   ├── password_checker.py
│   └── ... (other modules)
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_fizzbuzz.py
│   ├── test_greet.py
│   ├── test_counter.py
│   └── ... (other test files)
├── requirements.txt        # Project dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## 🧪 Test Coverage

This project maintains high test coverage with **43 passing tests** covering:
- Edge cases and boundary conditions
- Error handling and exceptions
- Normal operation scenarios
- Class state management
- Function return values

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Ensure all tests pass (`python -m pytest tests/`)
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 About The Golden Square

This project follows "The Golden Square" methodology of test-driven development, emphasizing:
- Write tests first
- Make tests pass with minimal code
- Refactor while keeping tests green
- Maintain high test coverage
- Clear, readable code and tests

## 📚 Learning Resources

This project serves as an excellent resource for learning:
- Test-Driven Development (TDD)
- Python testing with pytest
- Clean code principles
- Object-oriented programming
- Error handling best practices