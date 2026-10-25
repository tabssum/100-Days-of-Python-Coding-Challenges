# Day 04: List and String Problem Solving

This folder contains five Python exercises focused on arrays, strings, and logic-based problem solving. Each program demonstrates a different approach to handling common interview-style challenges.

## 1) Move All Zeros to the End
File: `01_move_zeros.py`

Implementation details:
- Read the input list from the user.
- Traverse the list and collect all non-zero values into a new list.
- Append the required number of zeros at the end.
- Print the final list with zeros moved to the end.

Example:
- Input: `[0, 1, 0, 3, 12]`
- Output: `[1, 3, 12, 0, 0]`

Time complexity: O(n)
Space complexity: O(n)

## 2) Find Common Elements in Two Lists
File: `02_common_elements.py`

Implementation details:
- Read two integer lists from the user.
- Convert both lists into sets.
- Use set intersection to find elements present in both.
- Print the common values only once.

Example:
- List 1: `[1, 2, 3, 4]`
- List 2: `[3, 4, 5, 6]`
- Output: `[3, 4]`

Time complexity: O(n + m)
Space complexity: O(n + m)

## 3) Find the First Non-Repeating Character
File: `03_first_non_repeating_character.py`

Implementation details:
- Read a string from the user.
- Loop through each character.
- Count how many times each character appears in the string.
- The first character whose count is exactly 1 is printed.
- If no such character exists, display a message.

Example:
- Input: `"swiss"`
- Output: `w`

Time complexity: O(n^2) using repeated `count()` calls
Space complexity: O(1) (ignoring the string itself)

## 4) Check Whether Two Strings Are Anagrams
File: `04_anagram_checker.py`

Implementation details:
- Read two strings from the user.
- Convert both to lowercase to ignore case.
- Build frequency dictionaries for each string.
- Compare both dictionaries.
- If the dictionaries match, the strings are anagrams.

Example:
- Input: `"Listen"`, `"Silent"`
- Output: `Anagram`

Time complexity: O(n)
Space complexity: O(k), where k is the number of unique characters

## 5) Find the Missing Number in a Sequence
File: `05_missing_number.py`

Implementation details:
- Read a list of numbers from the user.
- Determine the smallest and largest values in the list.
- Check every integer in that range.
- If a value is not present in the list, print it as the missing number.
- Stop at the first missing value found.

Example:
- Input: `[1, 2, 4, 5, 6]`
- Output: `Missing number is : 3`

Time complexity: O(n + range)
Space complexity: O(1)

## Summary
These exercises help build strong foundations in:
- list manipulation
- set operations
- string processing
- frequency counting
- logic-based problem solving

They are ideal for practicing Python interview questions and algorithmic thinking.
