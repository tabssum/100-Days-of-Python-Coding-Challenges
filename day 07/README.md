# Day 07: Functional Tools with `map()`, `filter()`, and `reduce()`

This folder practices Python's functional-style tools for transforming, selecting, and combining data. The exercises use `map()` to transform values, `filter()` to keep values that meet a condition, and `functools.reduce()` to accumulate a single result.

## Folder Contents

- `01_number_square_with_map_fun.py` — square every number in a list using `map()` and a lambda
- `02_add_two_lists_map.py` — intended to add corresponding elements of two lists with `map()`; implementation is currently empty
- `03_even_numbers_with_filter_func.py` — select even numbers from a list using `filter()`
- `04_remove_empty_str_filter_func.py` — filter empty strings from a list using `filter()`
- `05_sum_of_num_reduce_function.py` — calculate the sum and product of a list using `reduce()`

---

## 1. `01_number_square_with_map_fun.py`

### Problem
Create a list containing the square of each number in a user-provided list.

### Implementation details
- Reads space-separated integers and converts them with `map(int, ...)`.
- Applies a lambda that multiplies each number by itself using `map()`.
- Converts the resulting iterator to a list and prints it.

### Example
```text
Enter a list of numbers to caculate the square of each number: 2 3 4
The square of each number in the list is:  [4, 9, 16]
```

### Complexity
- Time: O(n)
- Space: O(n) for the input and result lists

---

## 2. `02_add_two_lists_map.py`

### Intended problem
Add corresponding elements of two lists using `map()`.

### Implementation status
The file currently contains only the problem statement; it does not yet read input, add values, or print a result. No working example or runtime complexity can be given until the solution is implemented.

---

## 3. `03_even_numbers_with_filter_func.py`

### Problem
Select the even numbers from a user-provided list of integers.

### Implementation details
- Reads space-separated integers and converts them to a list.
- Uses `filter()` with a lambda that checks whether `x % 2 == 0`.
- Converts the filtered iterator to a list and prints it.

### Example
```text
Enter a list of numbers:= 1 2 3 4 5 6
List of even numbers from the given list is: [2, 4, 6]
```

### Complexity
- Time: O(n), as each number is checked once
- Space: O(n) in the worst case for the result list

---

## 4. `04_remove_empty_str_filter_func.py`

### Problem
Keep non-empty strings from a list using `filter()`.

### Implementation details
- Reads whitespace-separated text and stores the tokens in a list.
- Uses `filter()` with a lambda that keeps values not equal to `""`.
- Converts the filtered iterator to a list and prints it.

Because the input is split on whitespace, blank entries are discarded before filtering; as written, the script normally receives no empty strings to remove. The filter demonstrates the intended operation if empty strings are present in the list.

### Example
```text
Enter a list of strings:= apple banana
List of non-empty strings from the given list is: ['apple', 'banana']
```

### Complexity
- Time: O(n), where n is the number of input tokens
- Space: O(n) for the input and filtered lists

---

## 5. `05_sum_of_num_reduce_function.py`

### Problem
Use `reduce()` to calculate both the sum and product of a list of integers.

### Implementation details
- Reads space-separated integers and converts them to a list.
- Imports `reduce` from `functools`.
- Uses addition in a lambda to accumulate the sum, then multiplication to accumulate the product.
- Prints both results.

### Example
```text
Enter a elements in first list:= 2 3 4
The sum of all numbers in the given list is: 9
The product of all numbers in the given list is: 24
```

### Complexity
- Time: O(n) for each reduction
- Space: O(n) for the input list; each reduction itself uses O(1) additional space

The script expects at least one number: `reduce()` without an initial value raises an error for an empty list.

---

## Learning Goals for Day 07

By the end of these exercises, you should be able to:
- use `map()` to transform each item in an iterable
- use `filter()` to select items that satisfy a condition
- use `reduce()` to combine values into one result
- write simple lambda expressions for these operations
- reason about the limits and edge cases of the current implementations

## Running the Scripts

From the repository root, run an implemented script with Python:

```bash
python "day 07/01_number_square_with_map_fun.py"
python "day 07/03_even_numbers_with_filter_func.py"
python "day 07/04_remove_empty_str_filter_func.py"
python "day 07/05_sum_of_num_reduce_function.py"
```

`02_add_two_lists_map.py` is not runnable as a completed exercise yet because it contains no implementation.
