# Day 03: Number Manipulation and Digit-Based Challenges

This folder focuses on beginner-friendly number operations using arithmetic, loops, and digit-by-digit processing. These challenges help build logic skills and strengthen understanding of common interview-style Python problems involving numbers, lists, and data counting.

## Folder Contents

- `01_sum_of_digits.py` — calculate the sum of all digits in a number
- `02_reverse_number.py` — reverse the digits of a number
- `03_armstrong_number.py` — check whether a number is an Armstrong number
- `04_element_frequency.py` — count how often each element appears in a list
- `05_second_largest.py` — find the second-largest distinct number in a list

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
Each iteration extracts the last digit and appends it to the reverse result while shifting the current reversed value left by one decimal place. This preserves the digits in reverse order without using string conversion.

#### Time complexity
- Time: O(n)
- Space: O(1)

---

## 3. `03_armstrong_number.py`

### Problem
Write a Python program to check whether a given number is an Armstrong number.

### Approach: Sum of each digit raised to the power of the number of digits
An Armstrong number is a number whose digits, when each is raised to the power of the total number of digits, sum to the original value.

- `str(number)` converts the number to a string so you can count digits.
- A loop runs through each digit.
- Each digit is raised to the power of `len(str(number))`.
- The result is added and compared with the original number.

#### Example
```python
Enter a number to check Armstrong number: = 153
153 is an Armstrong number
```

#### Why this works
For `153`, the digits are `1`, `5`, and `3`, and `1^3 + 5^3 + 3^3 = 153`. This matches the original value, so it is an Armstrong number.

#### Time complexity
- Time: O(n)
- Space: O(1)

---

## 4. `04_element_frequency.py`

### Problem
Write a Python program to count how many times each element appears in a list and store the results in a dictionary.

### Implementation details
- The input is read as a list of space-separated values.
- `set(ele_lst)` removes duplicate entries so the loop processes unique values only.
- `ele_lst.count(ele)` counts how many times each value appears.
- The result is stored in a dictionary where the key is the element and the value is its frequency.

#### Example
```python
Enter a list of numbers to count its frequency : = 1 2 2 3 1 2
Frequency of each element in a list is := {'1': 2, '2': 3, '3': 1}
```

#### Why this works
A dictionary maps each unique element to its count. By iterating through unique values and counting occurrences in the original list, we can build a frequency table efficiently and clearly.

#### Time complexity
- Time: O(n^2) in this implementation because `count()` is called for each unique value
- Space: O(n)

---

## 5. `05_second_largest.py`

### Problem
Write a Python program to find the second-largest distinct number in a list without using `sort()` or `sorted()`.

### Implementation details
- `lst_input = list(map(int, input(...).split()))` converts the user input into integers.
- `unique_ele = list(set(lst_input))` removes duplicates and keeps only distinct values.
- If there are fewer than two distinct values, the program prints a friendly message.
- Otherwise, it finds the largest value, removes it, and then finds the maximum remaining value.

#### Example
```python
Enter elements list to find second largest number : = 10 5 8 10 7
Second-largest number: 8
```

#### Why this works
The largest distinct value is removed from the set, leaving the second-largest value as the new maximum. This avoids sorting while still correctly handling duplicates and edge cases.

#### Time complexity
- Time: O(n)
- Space: O(n)

---

## Learning Goals for Day 03

By the end of this day, you should be able to:

- work with integer digit extraction
- use `while` loops for repetitive numeric logic
- understand modulo and integer division
- solve number-based interview problems efficiently
- compare multiple approaches to the same problem in Python
- recognize and validate Armstrong numbers
- count frequencies in lists using dictionaries
- identify the second-largest distinct element in a collection

## Running the Scripts

From the repository root, use the following commands:

```bash
python "day 03/01_sum_of_digits.py"
python "day 03/02_reverse_number.py"
python "day 03/03_armstrong_number.py"
python "day 03/04_element_frequency.py"
python "day 03/05_second_largest.py"
```

---

These exercises strengthen core Python fundamentals by focusing on arithmetic operations, loops, list processing, dictionary counting, and practical number-based problem solving.
