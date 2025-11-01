# AIE1001 Midterm Review Report

## Introduction
This report summarizes the key concepts and common error-prone areas from Weeks 1 to 6 of the AIE1001 Introduction to AI Programming course. Based on Week 8's Midterm Review slides, the exam (1 hour) includes single-choice (40 points), multiple-choice (15 points), and short-answer questions (45 points) on code fault localization, completion, and function design—no cheat sheets or calculators allowed.

## Week 1: Introduction to AI Programming
### Key Concepts
- **Number Systems**:
  - **Decimal**: Base 10, symbols {0,1,2,3,4,5,6,7,8,9}
  - **Binary**: Base 2, symbols {0,1}, "carry when hit 2"
  - **Octal**: Base 8, symbols {0,1,2,3,4,5,6,7}, "carry when hit 8"
  - **Hexadecimal**: Base 16, symbols {0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f}, "carry when hit 16"
- **Positional Notation**: N = a_n × base^n + a_{n-1} × base^{n-1} + ... + a_0 × base^0 + a_{-1} × base^{-1} + ...
  - a_n is the positional value, base^n is the weight

- **Number System Conversion Methods**:

  **1. Other Bases → Decimal**
  - Method: Expand using positional notation, multiply each digit by its weight, then sum
  - Example: Binary to decimal
    ```
    (10110.11)₂ = 1×2⁴ + 0×2³ + 1×2² + 1×2¹ + 0×2⁰ + 1×2⁻¹ + 1×2⁻²
                = 16 + 0 + 4 + 2 + 0 + 0.5 + 0.25
                = (22.75)₁₀
    ```
  - Octal to decimal: Same method, base is 8
    ```
    (35.7)₈ = 3×8¹ + 5×8⁰ + 7×8⁻¹ = 24 + 5 + 0.875 = (29.875)₁₀
    ```
  - Hexadecimal to decimal: Same method, base is 16
    ```
    (A7D.E)₁₆ = 10×16² + 7×16¹ + 13×16⁰ + 14×16⁻¹ = 2560 + 112 + 13 + 0.875 = (2685.875)₁₀
    ```

  **2. Decimal → Binary**
  - **Integer part**: Divide by 2, take remainder, from lower to higher position (last remainder is highest bit)
    ```
    Example: (57)₁₀ = (?)₂
    57 ÷ 2 = 28 ... remainder 1  ← lowest bit
    28 ÷ 2 = 14 ... remainder 0
    14 ÷ 2 = 7  ... remainder 0
    7  ÷ 2 = 3  ... remainder 1
    3  ÷ 2 = 1  ... remainder 1
    1  ÷ 2 = 0  ... remainder 1  ← highest bit
    Answer: (57)₁₀ = (111001)₂
    ```
  - **Fractional part**: Multiply by 2, take integer part, from higher to lower position (first integer part is highest bit)
    ```
    Example: (0.875)₁₀ = (?)₂
    0.875 × 2 = 1.75, integer part 1 ← highest bit
    0.75  × 2 = 1.5,  integer part 1
    0.5   × 2 = 1.0,  integer part 1 ← lowest bit
    Answer: (0.875)₁₀ = (0.111)₂
    ```
  - **Integer + fractional**: Convert integer and fractional parts separately, then combine
    ```
    Example: (215.6875)₁₀ = (?)₂
    Integer part: 215 = (11010111)₂
    Fractional part: 0.6875 = (0.1011)₂
    Answer: (215.6875)₁₀ = (11010111.1011)₂
    ```

  **3. Binary ↔ Octal**
  - **Binary → Octal**:
    - Integer part: Starting from lower (right) position, group every 3 binary digits, convert to 1 octal digit (pad with 0 at higher positions if needed)
    - Fractional part: Starting from higher (left) position, group every 3 binary digits, convert to 1 octal digit (pad with 0 at lower positions if needed)
    - Correspondence: 3 binary digits ↔ 1 octal digit
      ```
      (000)₂ = (0)₈    (001)₂ = (1)₈    (010)₂ = (2)₈    (011)₂ = (3)₈
      (100)₂ = (4)₈    (101)₂ = (5)₈    (110)₂ = (6)₈    (111)₂ = (7)₈
      ```
    - Example:
      ```
      (11010111.1011)₂ = (?)₈
      Integer part: 011 010 111 → 3 2 7
      Fractional part: 101 100 (pad 0) → 5 4
      Answer: (11010111.1011)₂ = (327.54)₈
      ```
  - **Octal → Binary**:
    - Convert each octal digit to 3 binary digits, keep order unchanged
    - Example:
      ```
      (327.54)₈ = (?)₂
      3 → 011,  2 → 010,  7 → 111
      5 → 101,  4 → 100
      Answer: (327.54)₈ = (011010111.101100)₂ = (11010111.1011)₂
      ```

  **4. Binary ↔ Hexadecimal**
  - **Binary → Hexadecimal**:
    - Integer part: Starting from lower (right) position, group every 4 binary digits, convert to 1 hexadecimal digit (pad with 0 at higher positions if needed)
    - Fractional part: Starting from higher (left) position, group every 4 binary digits, convert to 1 hexadecimal digit (pad with 0 at lower positions if needed)
    - Correspondence: 4 binary digits ↔ 1 hexadecimal digit (0-9 correspond to digits, 10-15 correspond to a-f)
    - Example:
      ```
      (11010111.1011)₂ = (?)₁₆
      Integer part: 1101 0111 → D 7
      Fractional part: 1011 0000 (pad 0) → B 0
      Answer: (11010111.1011)₂ = (D7.B)₁₆
      ```
  - **Hexadecimal → Binary**:
    - Convert each hexadecimal digit to 4 binary digits, keep order unchanged
    - Example:
      ```
      (D7.B)₁₆ = (?)₂
      D → 1101,  7 → 0111
      B → 1011
      Answer: (D7.B)₁₆ = (11010111.1011)₂
      ```

  **5. Decimal → Octal/Hexadecimal**
  - Method: First convert to binary, then convert to octal or hexadecimal
  - Or: Directly use division/multiplication with corresponding base (similar to decimal to binary)

- **Unit Conversion**: 1 KB = 1024 B (2^10), 1 MB = 1024 KB, 1 GB = 1024 MB.
- **Computer Fundamentals**: Von Neumann architecture, CPU (control unit and arithmetic/logic unit), memory (RAM/ROM), input/output devices.
- **Variables**: A variable is a named space in memory where values can be stored and retrieved. Integer variables are immutable.

### Common Pitfalls
- **Wrong direction for fractional part conversion**: Decimal to binary fraction goes from higher to lower position (first integer part is highest bit); integer part goes from lower to higher position (first remainder is lowest bit).
- **Forgetting to handle integer and fractional parts separately**: If a number has both parts, must convert separately then combine.
- **Forgetting to pad zeros when converting between binary and octal/hexadecimal**:
  - Octal: Group every 3 binary digits, pad with 0 if needed
  - Hexadecimal: Group every 4 binary digits, pad with 0 if needed
  - Integer part groups from lower position, fractional part groups from higher position
- **Wrong weights in positional notation expansion**: Note integer part weights start from 2⁰ (or 8⁰, 16⁰), fractional part weights start from 2⁻¹ (or 8⁻¹, 16⁻¹).

## Week 2: Python Basics
### Key Concepts
- **Interpreter vs. Compiler**: An interpreter directly executes code, while a compiler first converts to machine code. Python uses an interpreter, supporting interactive mode (line-by-line input) and script mode (file execution).
- **Variable Naming Rules**: Must start with a letter or underscore; can only contain letters, numbers, and underscores; case-sensitive; cannot use reserved words (e.g., def, if, while).
- **Data Types**: Integer (int), float (float), string (str). Use type() to check types.
- **Type Conversion**: int(), float(), str(). When an expression contains both integer and float, integers are implicitly converted to float.
- **Operators**: Arithmetic operators (+, -, *, /, //, %, **). // is floor division (e.g., -7//2 = -4). ** is exponentiation, right-associative (e.g., 2**3**2 = 2**(3**2) = 512). Operator precedence: parentheses > exponentiation > multiplication/division/remainder > addition/subtraction.
- **+ Operator Specific Usage**:
  - Strings: `'hello' + 'world'` = `'helloworld'` (concatenation)
  - Lists: `[1, 2] + [3, 4]` = `[1, 2, 3, 4]` (creates new list)
  - Numbers: `3 + 5` = `8` (arithmetic addition)
  - Note: Cannot add string and number (e.g., `'2' + 3` raises error), need type conversion first
- **Assignment**: = is for assignment; == is for comparison. Cascaded assignment: x = y = z = 0. Simultaneous assignment: x, y = y, x (swaps two variables).
- **Input/Output**: input() returns a string; print() for output.
- **eval() Function**:
  - `eval()` function takes a string argument and evaluates that string as a Python expression
  - Just as if the programmer had directly entered the expression as code, returns the result of that expression
  - Example: `eval('2 + 3')` returns `5`; `eval('3 * 4')` returns `12`
  - Purpose: Gives programmers flexibility to determine what to execute at run-time
  - **Security Warning**: Should be cautious about using it, as users could potentially cause problems with "inappropriate" input (e.g., executing dangerous operations like deleting files). If only processing numeric literals, prefer `int()` or `float()` instead of `eval()`

### Common Pitfalls
- Forgetting input() returns a string, leading to type errors in arithmetic (e.g., '2' + 3).
- Operator precedence mistakes (e.g., 1 + 2 * 3 = 7, not 9).
- Indentation errors in script mode (must use consistent spaces or tabs).
- Confusing = and == (= is assignment, == is comparison).
- Security concerns with eval() (executes arbitrary code, users may input dangerous operations; if only processing numbers, prefer int() or float()).

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
  - List + operator: `[1, 2] + [3, 4]` = `[1, 2, 3, 4]` (creates new list, doesn't modify original)
  - List * operator: `[1, 2] * 3` = `[1, 2, 1, 2, 1, 2]` (repeats)
- **range() Function**: Returns number sequence, used in for loops. For example, range(5) produces [0,1,2,3,4]. Note: range() in Python 3 returns a range object, not a list.
- **Dictionaries**: Use curly braces {}, key-value pairs {key: value}. Unordered collection (but Python 3.7+ preserves insertion order). Access value by key; KeyError if key doesn't exist.
- **get() Method Specific Usage**:
  - Syntax: `dict.get(key, default_value)`
  - If key exists, returns corresponding value; if key doesn't exist, returns default value (no error)
  - Example: `d = {'a': 1, 'b': 2}`, then `d.get('a', 0)` returns `1`, `d.get('c', 0)` returns `0`
  - If default not provided, returns None when key missing: `d.get('c')` returns `None`
- **Dictionary Counting Pattern**:
  ```python
  d = {}
  word = 'hello'
  d[word] = d.get(word, 0) + 1  # If word not in dict, returns 0 first, then adds 1
  ```
- **Dictionary Iteration Three Ways**:
  1. **Direct iteration**: `for key in d:` or `for key in d.keys():` - iterates over **keys**, not values. Need `d[key]` to get value.
  2. **Iterate values**: `for value in d.values():` - only iterates values, cannot directly get corresponding key
  3. **Iterate key-value pairs (recommended)**: `for key, value in d.items():` - uses two iteration variables to get both key and value
  - Example:
    ```python
    d = {'a': 1, 'b': 2}
    # Way 1: iterate keys
    for k in d:
        print(k, d[k])  # Output: a 1, b 2
    # Way 2: iterate key-value pairs
    for k, v in d.items():
        print(k, v)  # Output: a 1, b 2
    ```
  - Note: Direct iteration over dictionary (`for key in d`) actually iterates over keys, not values, not key-value pairs
- **Tuples**: Immutable sequences with parentheses (). Can be dictionary keys (because immutable). items() method returns list of (key, value) tuples.
- **Tuple Comparison**: Tuples are comparable, lexicographically (compares first element, then next if equal).
- **Sorting**: list.sort() sorts in-place; sorted() returns new list. Can sort dictionary items().

### Common Pitfalls
- Index out of range (lists/strings start at 0, len() excludes last index).
- Trying to modify tuple (TypeError: 'tuple' object does not support item assignment).
- KeyError when accessing non-existent dictionary key: Using `d['key']` on missing key raises error, should use `d.get('key', default)` or check `'key' in d` first.
- Misunderstanding dictionary iteration: `for item in d:` iterates over keys, need `d[item]` to get value, or use `for k, v in d.items()` directly.
- Confusing sort() and sorted() (former mutates list, latter returns new list).
- Using + instead of append() for list concatenation, causing efficiency issues:
  - `lst = lst + [x]` creates new list, inefficient (O(n))
  - `lst.append(x)` modifies original list, efficient (O(1) amortized)
  - Frequent use of `+` in loops is slow, should use `append()`

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
