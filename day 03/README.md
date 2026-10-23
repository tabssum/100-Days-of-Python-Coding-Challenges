# Day 03: Number Manipulation and Digit-Based Challenges

This folder focuses on beginner-friendly number operations using arithmetic, loops, and digit-by-digit processing. These challenges are useful for developing logic skills and understanding how to work with numeric data in Python.

## Folder Contents

- `01_sum_of_digits.py` — calculate the sum of all digits in a number
- `02_reverse_number.py` — reverse the digits of a number

---

## 1. `01_sum_of_digits.py`

### Problem
Write a Python program to calculate the sum of all digits in a given integer.

### Implementation details
- The program reads an integer using `input()`.
- It converts the number to a string and iterates through each character.
- Each digit is converted back to an integer and added to a running total.
- An alternative approach uses a `while` loop with `% 10` and `// 10` to repeatedly isolate digits.

### Example
```python
Enter a number to find its digits sum: = 12345
Sum of digits of a number 12345 is := 15
```

### Why this works
The digits of a number can be processed one at a time. By repeatedly extracting the last digit using modulo and then removing it with integer division, the program can add every digit efficiently.

### Time complexity
- Time: O(n)
- Space: O(n) in the string-based approach

---

## 2. `02_reverse_number.py`

### Problem
Write a Python program to reverse the digits of a given integer without converting it into a string.

### Implementation details
- The program reads an integer from the user.
- One solution uses string slicing with `[::-1]` to reverse the digits.
- Another approach uses a `while` loop, `% 10`, and `// 10` to rebuild the reversed number.

### Example
```python
Enter a number to reverse it : = 1234
Reversed number of a number 1234 is := 4321
```

### Why this works
When a number is divided by 10, the last digit is isolated. By multiplying the reversed result by 10 and adding the extracted digit repeatedly, the original digits are reordered in reverse.

### Time complexity
- Time: O(n)
- Space: O(1)

---

## Learning Goals for Day 03

By the end of this day, you should be able to:
- work with integer digit extraction
- use `while` loops for repetitive numeric logic
- understand modulo and integer division
- solve number-based interview problems efficiently
- build confidence in writing clear logic-based Python programs

## Running the Scripts

From the repository root, use the following commands:

```bash
python "day 03/01_sum_of_digits.py"
python "day 03/02_reverse_number.py"
```

---

These exercises help strengthen core Python fundamentals by focusing on arithmetic operations, loops, and practical number-processing patterns.
