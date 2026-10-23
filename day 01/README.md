# Day 01: Python Basics and Core Logic Challenges

This folder focuses on beginner-level Python problem solving using conditionals, loops, and simple input/output. These exercises help build strong foundations in logic, number operations, and string handling.

## Folder Contents

- `01_even_odd.py` — determine whether a number is even or odd
- `02_palindrome.py` — check if a string reads the same backward
- `03_factorial.py` — calculate the factorial of a given number
- `05_prime.py` — check whether a number is prime

---

## 1. `01_even_odd.py`

### Problem
Write a Python program to check whether a user-entered number is even or odd.

### Implementation details
- The program reads an integer using `input()`.
- It uses the modulus operator `%` to test divisibility by 2.
- A conditional expression prints the result.

### Example
```python
Enter a number:= 8
Number is even
```

### Why this works
If a number divided by 2 leaves no remainder, it is even; otherwise it is odd. The `%` operator is used to check that remainder.

### Time complexity
- Time: O(1)
- Space: O(1)

---

## 2. `02_palindrome.py`

### Problem
Check whether a string is a palindrome.

### Implementation details
- The user enters a string.
- The program creates a reversed version using slicing: `str_input[::-1]`.
- It compares the original string with the reversed string.

### Example
```python
Enter a string to check whether its palindrome or not := level
String is palindrome
```

### Why this works
A palindrome reads the same forwards and backwards. Reversing the string and comparing it with the original is a simple and effective test.

### Time complexity
- Time: O(n)
- Space: O(n)

---

## 3. `03_factorial.py`

### Problem
Find the factorial of a number entered by the user.

### Implementation details
- The program reads an integer input.
- It checks whether the number is negative.
- If the number is non-negative, a loop multiplies each value from `num` down to `1`.

### Example
```python
Enter a number to find factorial: 5
Factorial of a number 5 is : 120
```

### Why this works
Factorial is the product of all positive integers from 1 to `n`. A loop repeatedly multiplies the running total by each decreasing value.

### Time complexity
- Time: O(n)
- Space: O(1)

---

## 4. `05_prime.py`

### Problem
Check whether a number is prime or not.

### Implementation details
- The program asks the user for an integer.
- If the number is less than 2, it is immediately considered not prime.
- Otherwise, the code tests divisibility by all integers from 2 to `sqrt(number)`.
- If no divisor is found, the number is prime.

### Example
```python
Enter a number to check whether its prime or not := 13
Number is prime
```

### Why this works
A prime number has no divisors other than 1 and itself. Checking up to the square root of the number is enough because any larger factor would have a corresponding smaller factor.

### Time complexity
- Time: O(sqrt(n))
- Space: O(1)

---

## Learning Goals for Day 01

By the end of this day, you should be able to:
- use basic arithmetic operators effectively
- write conditional statements in Python
- work with loops and repetition
- manipulate strings using slicing
- solve simple problem-solving tasks used in coding interviews

## Running the Scripts

From the repository root, use any of the following commands:

```bash
python "day 01/01_even_odd.py"
python "day 01/02_palindrome.py"
python "day 01/03_factorial.py"
python "day 01/05_prime.py"
```

---

These exercises introduce the core logic patterns that are used throughout Python programming and interview preparation.
