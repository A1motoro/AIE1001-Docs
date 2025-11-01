# AIE1001 Midterm Review Report

## Introduction
This report summarizes the key concepts and common error-prone areas from Weeks 1 to 6 of the AIE1001 Introduction to AI Programming course. The midterm exam covers these topics, focusing on Python basics, control structures, functions, data structures, and recursion. Understanding these fundamentals is crucial for programming AI applications.

## Week 1: Introduction to AI Programming
### Key Concepts
- **Computer Fundamentals**: Von Neumann architecture, CPU, memory (RAM/ROM), input/output devices.
- **AI Impact**: Historical revolutions, AI applications (e.g., AlphaFold, self-driving cars), limitations (robustness, data reliance).
- **Programming Languages**: Evolution from assembly to Python; efficiency vs. development speed.
- **Number Systems**: Binary, decimal, octal, hexadecimal conversions; positional notation; units (bit, byte, KB, etc.).
- **Data Representation**: Memory addressing, abstraction layers (hardware to apps).

### Common Pitfalls
- Errors in converting fractional parts between number systems (e.g., decimal to binary multiplication by 2).
- Confusing bases in conversions (e.g., forgetting to pad with zeros for octal/binary).
- Misunderstanding why binary is used (physical implementation) and its relation to hexadecimal (grouping 4 bits).
- Overlooking that variables reference memory locations, not store values directly.

## Week 2: Python Basics
### Key Concepts
- **Interpreter vs. Compiler**: Python uses an interpreter for interactive/script mode.
- **Variables and Data Types**: Naming rules, constants (uppercase), int/float/str, type() function.
- **Type Conversion**: int(), float(), str(); implicit conversion in mixed expressions.
- **Expressions and Operators**: Arithmetic (+, -, *, /, //, %, **), precedence (PEMDAS), augmented assignment (+=, etc.).
- **Input/Output**: input() returns str; print() for output; eval() for dynamic evaluation.
- **Strings**: Concatenation (+, *), indexing.

### Common Pitfalls
- Forgetting input() returns a string, leading to type errors in arithmetic (e.g., '2' + 3).
- Operator precedence mistakes (e.g., 1 + 2 * 3 = 7, not 9).
- Indentation errors in scripts.
- Using == for assignment instead of =.
- Infinite loops from incorrect conditions in while loops.
- Misusing eval() with unsafe input.

## Week 3: Flow Control
### Key Concepts
- **Comparisons**: ==, !=, <, >, <=, >=; string lexicographical comparison (ASCII/Unicode).
- **Boolean**: True/False, bool(), logical operators (and, or, not).
- **Conditionals**: if, elif, else; nested ifs; multi-way decisions.
- **Loops**: while (indefinite), for (definite) with range(); break, continue.
- **Exception Handling**: try/except for errors like ValueError.
- **Floating-Point**: Precision issues in comparisons.

### Common Pitfalls
- Floating-point precision (e.g., 0.1 + 0.2 != 0.3 due to approximation).
- Case-sensitive string comparisons; ignoring Unicode for non-ASCII chars.
- Off-by-one errors in loop conditions (e.g., while i < len(s) vs. <=).
- Indentation inconsistencies causing syntax errors.
- Forgetting else in two-way decisions or misplacing elif.
- Infinite loops without proper termination conditions.

## Week 4: Functions
### Key Concepts
- **Definition**: def, parameters vs. arguments, return vs. void (None).
- **Scope**: Local vs. global variables; use global keyword cautiously.
- **Advanced**: Default arguments, multiple returns (tuples), nested calls.
- **Fruitful Functions**: Return values for reuse; void for side effects (e.g., print).

### Common Pitfalls
- Parameter order mismatches in calls.
- Scope errors: modifying local var doesn't affect global; accidental global use.
- Forgetting return statement, leading to None.
- Recursion depth exceeded (though basic recursion introduced later).
- Default args evaluated at definition, not call (mutable defaults pitfall).
- Overusing global variables, leading to hard-to-debug code.

## Week 5: Lists, Dictionaries, and Tuples
### Key Concepts
- **Lists**: Mutable sequences [ ], indexing/slicing, len(), append(), sort(), in operator; built-ins (max, min, sum).
- **Dictionaries**: {key: value}, unordered, get(), keys()/values()/items(); counting with dicts.
- **Tuples**: Immutable (), efficient for fixed data; comparable for sorting.
- **Operations**: Concat (+), repeat (*), split() for strings to lists.
- **Sorting**: list.sort() (in-place) vs. sorted(); sorting dicts by key/value.

### Common Pitfalls
- Index out of range (lists/strings start at 0, len() excludes last index).
- Modifying tuples (immutable error).
- KeyError in dict access; forgetting get() for defaults.
- Assuming dict order (Python 3.7+ preserves insertion, but not guaranteed).
- Confusion between list methods (e.g., sort() vs. sorted()).
- Infinite loops when building lists without append() properly.

## Week 6: Recursion
### Key Concepts
- **Recursion Basics**: Base case (no calls), recursive case (calls self with smaller input).
- **Examples**: Factorial (n! = n * (n-1)!), power (x^n), binary search (sorted lists).
- **Linear Recursion**: One recursive call (e.g., sum list).
- **Multiple Recursion**: Multiple calls (e.g., Fibonacci, English ruler).
- **Efficiency**: Stack frames for calls; tail recursion optimization (not in Python).

### Common Pitfalls
- Missing or incorrect base case, causing infinite recursion (e.g., fact(0) not handled).
- Off-by-one in recursive conditions (e.g., n-1 when n==1).
- Stack overflow from deep recursion (Python limit ~1000 calls).
- Misunderstanding call stack: each call has own frame, returns unwind.
- Inefficient multiple recursion (e.g., Fibonacci recomputes values).
- Forgetting to reduce problem size in recursive case.

## Conclusion
Focus on practicing code execution mentally or with Python Tutor for recursion and loops. Common errors often stem from types, scopes, and off-by-one indices. Review number systems and floating-point for edge cases. For the exam, emphasize writing correct Python code for functions, loops, and recursive solutions. Good luck!
