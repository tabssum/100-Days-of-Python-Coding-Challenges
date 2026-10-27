# Day 05: Python Basics and Data Structure Practice

This folder contains five Python challenges focused on list handling, strings, dictionaries, and number logic. Each script demonstrates a practical problem-solving pattern and includes a simple interactive input flow.

## Files Included

### 1) 01_maximum-difference.py
**Problem:** Find the maximum difference between any two numbers in a list.

**Implementation details:**
- Reads user input as integers from a space-separated list.
- Uses `min()` and `max()` to find the smallest and largest elements.
- Computes the difference as `max_value - min_value`.
- Prints the result in a user-friendly format.

**Time complexity:** O(n)  
**Space complexity:** O(1)

### 2) 02_remove_duplicate_char.py
**Problem:** Remove duplicate characters while preserving the original order.

**Implementation details:**
- Iterates through the string character by character.
- Checks whether the character already exists in a list called `unique_char`.
- Appends only the first occurrence to preserve order.
- Joins the list back into a string and prints the result.

**Time complexity:** O(n^2) in the worst case because membership testing in a list is linear.  
**Space complexity:** O(n)

### 3) 03-group-words-by-length.py
**Problem:** Group words by their length using a dictionary.

**Implementation details:**
- Splits the input string into individual words.
- Computes `len(word)` for each word.
- Uses a dictionary where the key is word length and the value is a list of words with that length.
- Appends each word to its corresponding list.
- Prints the final dictionary.

**Time complexity:** O(n) for processing words, assuming average string length is constant.  
**Space complexity:** O(n)

### 4) 04-perfect-number.py
**Problem:** Check whether a number is a perfect number.

**Implementation details:**
- Loops through values from 1 to `num - 1`.
- Checks each value using modulo `%` to find divisors.
- Adds all proper divisors to a running sum.
- Compares the sum with the original number.
- Prints whether the number is perfect or not.

**Time complexity:** O(n)  
**Space complexity:** O(1)

### 5) 05-merge-dictionaries.py
**Problem:** Merge two dictionaries and add values for matching keys.

**Implementation details:**
- Creates a copy of `dict1` to preserve its original data.
- Iterates over each key in `dict2`.
- If the key already exists, adds the second value to the first.
- Otherwise, adds the new key-value pair.
- Prints the merged dictionary.

**Time complexity:** O(n)  
**Space complexity:** O(n)

## Summary
These exercises strengthen core Python concepts such as:
- Lists and loops
- Strings and membership checks
- Dictionaries and grouping logic
- Division / modulo operations
- Basic dictionary merging and accumulation

This set is a good foundation for understanding how to manipulate common data structures in Python.
