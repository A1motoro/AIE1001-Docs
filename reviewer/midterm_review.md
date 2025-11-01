# AIE1001 Midterm Review Report

## Introduction
This report summarizes the key concepts and common error-prone areas from Weeks 1 to 6 of the AIE1001 Introduction to AI Programming course. Based on Week 8's Midterm Review slides, the exam (1 hour) includes single-choice (40 points), multiple-choice (15 points), and short-answer questions (45 points) on code fault localization, completion, and function design—no cheat sheets or calculators allowed.

## Week 1: Introduction to AI Programming
### Key Concepts
- **Number System Conversions**: Conversions between decimal, binary, octal, and hexadecimal. Positional notation: N = a_n × base^n + a_{n-1} × base^{n-1} + ... + a_0 × base^0 + a_{-1} × base^{-1} + ... Note: When converting decimal fractions to binary, multiply the fractional part by 2, take the integer part as the next digit, from higher to lower position.
- **Unit Conversion**: 1 KB = 1024 B (2^10), 1 MB = 1024 KB, 1 GB = 1024 MB.
- **Computer Fundamentals**: Von Neumann architecture, CPU (control unit and arithmetic/logic unit), memory (RAM/ROM), input/output devices.
- **Variables**: A variable is a named space in memory where values can be stored and retrieved. Integer variables are immutable.

### Common Pitfalls
- Forgetting the direction when converting fractional parts: decimal to binary fractions go from higher to lower position; integer parts go from lower to higher position.
- Forgetting to handle integer and fractional parts separately: if a number has both parts, convert them separately and combine.
- Forgetting to pad zeros when converting between binary and octal/hexadecimal: octal groups 3 binary digits, hexadecimal groups 4 binary digits.

## Week 2: Python Basics
### Key Concepts
- **Interpreter vs. Compiler**: An interpreter directly executes code, while a compiler first converts to machine code. Python uses an interpreter, supporting interactive mode (line-by-line input) and script mode (file execution).
- **Variable Naming Rules**: Must start with a letter or underscore; can only contain letters, numbers, and underscores; case-sensitive; cannot use reserved words (e.g., def, if, while).
- **Data Types**: Integer (int), float (float), string (str). Use type() to check types.
- **Type Conversion**: int(), float(), str(). When an expression contains both integer and float, integers are implicitly converted to float.
- **Operators**: Arithmetic operators (+, -, *, /, //, %, **). // is floor division (e.g., -7//2 = -4). ** is exponentiation, right-associative. Operator precedence: parentheses > exponentiation > multiplication/division/remainder > addition/subtraction.
- **Assignment**: = is for assignment; == is for comparison. Cascaded assignment: x = y = z = 0. Simultaneous assignment: x, y = y, x (swaps two variables).
- **Input/Output**: input() returns a string; print() for output; eval() can execute a string as a Python expression.

### Common Pitfalls
- Forgetting input() returns a string, leading to type errors in arithmetic (e.g., '2' + 3).
- Operator precedence mistakes (e.g., 1 + 2 * 3 = 7, not 9).
- Indentation errors in script mode (must use consistent spaces or tabs).
- Confusing = and == (= is assignment, == is comparison).
- Security concerns with eval() (executes arbitrary code).

## Week 3: Flow Control
### Key Concepts
- **Comparison Operators**: ==, !=, <, >, <=, >=. Note: = is for assignment, == is for comparison.
- **String Comparison**: Lexicographical comparison based on ASCII/Unicode code points. For example, 'A' < 'a' (ASCII 'A'=65, 'a'=97).
- **Floating-Point Comparison**: Floating-point numbers are approximations; 0.1 cannot be exactly represented (e.g., 0.1 + 0.2 ≠ 0.3). Python's float is IEEE-754 double-precision (64 bits), can only store about 15–17 significant decimal digits precisely.
- **Boolean Type**: True/False. Number 0 represents False; all other numbers represent True. Falsy values include: None, False, 0/0.0/0j, empty sequences/collections ("", [], {}, set(), range(0)). Everything else is truthy.
- **Conditional Statements**: if (one-way), if-else (two-way), if-elif-else (multi-way). Note indentation and elif placement.
- **Loops**: while (indefinite loop, stops when condition is False), for (definite loop, iterates over sequences). range() function generates number sequences. break exits loop, continue skips current iteration.
- **Exception Handling**: try/except catches errors (e.g., ValueError).

### Common Pitfalls
- Floating-point precision issues (e.g., 0.1 + 0.2 == 0.30000000000000004).
- Ignoring case sensitivity and Unicode characters in string comparisons.
- Off-by-one errors in loop conditions (e.g., while i < len(s) vs. i <= len(s)).
- Indentation inconsistencies causing syntax errors.
- Forgetting else or misplacing elif.
- Infinite loops (missing termination condition or forgetting to update loop variable).

## Week 4: Functions
### Key Concepts
- **Function Definition**: def function_name(parameters): function_body. Function signature indicates function name and number of parameters.
- **Parameters and Arguments**: Parameter is a variable in function definition; argument is a value passed when calling.
- **Return Values**: return statement returns result and ends function execution. Returns None if no return (void function).
- **Scope**: Local variables (defined inside function) and global variables (defined outside function). Use global keyword to declare global variable inside function (use with caution).
- **Default Arguments**: Function parameters can have default values; callers can omit those arguments.
- **Return Multiple Values**: Can return multiple values (actually a tuple), receive with simultaneous assignment (e.g., x, y = func()).

### Common Pitfalls
- Parameter order or count mismatch when calling.
- Scope errors: modifying local variable doesn't affect global; accidental global use.
- Forgetting return statement, leading to None return.
- Default arguments evaluated at function definition time (if default is mutable object like list, shares same object).
- Overusing global variables, making code hard to debug.

## Week 5: Lists, Dictionaries, and Tuples
### Key Concepts
- **Lists**: Mutable sequences with square brackets []. Access elements by index (starts at 0). len() returns length. append() adds element. sort() sorts in-place. Can concatenate with +, repeat with *. Slicing similar to strings (second number is "up to but not including").
- **range() Function**: Returns number sequence, used in for loops. For example, range(5) produces [0,1,2,3,4]. Note: range() in Python 3 returns a range object, not a list.
- **Dictionaries**: Use curly braces {}, key-value pairs {key: value}. Unordered collection (but Python 3.7+ preserves insertion order). Access value by key; KeyError if key doesn't exist. Use get() method to get value with default if key missing.
- **Dictionary Counting**: Common pattern: d[word] = d.get(word, 0) + 1 to count frequencies.
- **Dictionary Iteration**: Can iterate over keys with for loop; keys(), values(), items() methods. Can use two iteration variables: for k, v in d.items().
- **Tuples**: Immutable sequences with parentheses (). Can be dictionary keys (because immutable). items() method returns list of (key, value) tuples.
- **Tuple Comparison**: Tuples are comparable, lexicographically (compares first element, then next if equal).
- **Sorting**: list.sort() sorts in-place; sorted() returns new list. Can sort dictionary items().

### Common Pitfalls
- Index out of range (lists/strings start at 0, len() excludes last index).
- Trying to modify tuple (TypeError: 'tuple' object does not support item assignment).
- KeyError when accessing non-existent dictionary key (should use get() or check with in first).
- Confusing sort() and sorted() (former mutates list, latter returns new list).
- Using + instead of append() for list concatenation, causing efficiency issues (e.g., lst = lst + [x] is O(n), while append() is O(1)).

## Week 6: Recursion
### Key Concepts
- **Recursion Concept**: Function calls itself. Recursive definition contains: base case (simple situation, no recursion needed) and recursive case (reduces problem to smaller version).
- **Factorial Example**: n! = n × (n-1)!, base case is 0! = 1.
- **Recursion Implementation**: Python creates activation record (frame) for each function call, storing parameters and local variables. Function call pauses current function, records return location; last called, first to finish.
- **Environment Diagrams**: Can draw environment diagrams to trace recursion; each call has its own frame; value of n depends on current environment.
- **Recursive Tree**: Another way to visualize recursion, showing function call tree.
- **Binary Search**: Recursive search algorithm for sorted lists. Maintains low and high parameters, compares middle element data[mid], recurses left half if target smaller, right half if larger.
- **Linear Recursion**: Each call makes at most one recursive call (e.g., factorial, binary search).
- **Multiple Recursion**: Each call makes two or more recursive calls (e.g., Fibonacci, English ruler drawing).

### Common Pitfalls
- Missing or incorrect base case, causing infinite recursion (e.g., fact(0) not handled).
- Recursive condition errors (e.g., n-1 when n==1).
- Stack overflow from deep recursion (Python default recursion limit ~1000).
- Misunderstanding call stack: each call has own frame, unwinds on return.
- Inefficient multiple recursion (e.g., Fibonacci recomputes values; should use memoization or dynamic programming).
- Forgetting to reduce problem size in recursive case (e.g., fact(n) = n * fact(n) loops forever).

## Conclusion
Focus on practicing code execution (use Python Tutor to visualize recursion and loops). Common errors often stem from types, scopes, and off-by-one indices. Review number system conversions and floating-point precision issues. From Week 8 Midterm Review, expect questions on: conversions (e.g., binary fractions), loops (e.g., range list comprehensions), dictionaries (e.g., get() for counting), recursion traces (environment diagrams), and code debugging (e.g., tuple immutability errors, KeyError). For short answers, practice locating faults (e.g., missing base case) and completing code (e.g., recursive sum). For the exam, emphasize writing correct Python code for functions, loops, and recursive solutions. Good luck!
