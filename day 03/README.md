# Day 03: Number Manipulation and Digit-Based Challenges

This folder focuses on beginner-friendly number operations using arithmetic, loops, and digit-by-digit processing. These challenges help build logic skills and strengthen understanding of common interview-style tasks involving integers.

## Folder Contents

- `01_sum_of_digits.py` — calculate the sum of all digits in a number
- `02_reverse_number.py` — reverse the digits of a number

---

## 1. `01_sum_of_digits.py`

### Problem
Write a Python program to calculate the sum of all digits in a given integer.

### Approach 1: String conversion + loop
This implementation converts the number into a string and then iterates through each character.

- `str(number)` turns the integer into a sequence of digits.
- A `for` loop goes through each character.
- Each digit is converted back to an integer and added to a list.
- `sum(digit_list)` returns the total.

#### Example
```python
Enter a number to find its digits sum: = 12345
Sum of digits of a number 12345 is := 15
```

#### Why this works
Each digit in a number can be processed individually. By turning the number into text, we can visit each digit in order and add them together.

#### Time complexity
- Time: O(n)
- Space: O(n)

### Approach 2: Modulo and integer division
This version avoids converting the number to a string and instead uses arithmetic operations.

- `digit = number % 10` extracts the last digit.
- `sum_of_digits += digit` adds it to the running total.
- `number = number // 10` removes the final digit.
- The loop keeps going until the number becomes `0`.

#### Example
```python
Enter a number to find its digits sum: = 12345
Sum of digits of a number 12345 is := 15
```

#### Why this works
Repeatedly taking the remainder by 10 gives the rightmost digit, while integer division removes that digit. This is a classic technique for working with digits in numeric form.

#### Time complexity
- Time: O(n)
- Space: O(1)

---

## 2. `02_reverse_number.py`

### Problem
Write a Python program to reverse the digits of a given integer.

### Approach 1: String slicing
The first solution converts the number to a string and reverses it using slicing.

- `str(number)` converts the integer to text.
- `[::-1]` reverses the string in a single operation.
- The reversed value is printed.

#### Example
```python
Enter a number to reverse it : = 1234
Reversed number of a number 1234 is := 4321
```

#### Why this works
Python string slicing with a negative step walks backward through the value, so a number like `1234` becomes `4321` efficiently and clearly.

#### Time complexity
- Time: O(n)
- Space: O(n)

### Approach 2: While loop with modulo and division
The second implementation keeps the number as an integer and rebuilds the reversed value step by step.

- `digit = number % 10` extracts the last digit.
- `reversed_number = reversed_number * 10 + digit` appends the digit to the result.
- `number = number // 10` removes the last digit from the original value.
- The loop continues until the original number is empty.

#### Example
```python
Enter a number to reverse it:= 1234
Reversed number of a number 1234 is := 4321
```

#### Why this works
Each iteration extracts the last digit and appends it to the reverse result while shifting the current reversed value left by one decimal place. This preserves the digits in reverse order without converting the value to a string.

#### Time complexity
- Time: O(n)
- Space: O(1)

---

## Learning Goals for Day 03

By the end of this day, you should be able to:

- work with integer digit extraction
- use `while` loops for repetitive numeric logic
- understand modulo and integer division
- solve number-based interview problems efficiently
- compare multiple approaches to the same problem in Python

## Running the Scripts

From the repository root, use the following commands:

```bash
python "day 03/01_sum_of_digits.py"
python "day 03/02_reverse_number.py"
```

---

These exercises strengthen core Python fundamentals by focusing on arithmetic operations, loops, and practical number-processing patterns.
