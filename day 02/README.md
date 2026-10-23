# Day 02: String and List Manipulation Challenges

This folder focuses on common beginner-to-intermediate Python problem patterns involving string processing, counting, and list operations. These exercises are useful for interview preparation, practice, and improving logic-building skills.

## Folder Contents

- `01_reverse_string.py` — reverse a string without using a built-in reverse function
- `02_count_vowels_consonants.py` — count vowels and consonants in a sentence
- `03_largest_number.py` — find the maximum value in a list
- `04_remove_duplicates.py` — delete repeated entries while preserving order
- `05_character_frequency.py` — count how many times each character appears

---

## 1. `01_reverse_string.py`

### Problem
Write a Python program that reverses a user-provided string without using a built-in reverse method.

### Implementation details
- The program reads text using `input()`.
- Python slicing with `[::-1]` reverses the sequence efficiently.
- The formatted output prints the reversed value along with the original string.

### Example
```python
Enter a string to reverse it := python
Reversed string is := nohtyp of original string python
```

### Why slicing works
In Python, `string[start:end:step]` allows slicing with a negative step to move backward through the string. Using `[::-1]` means "start from the end, move to the beginning, and include every character."

### Time complexity
- Time: O(n)
- Space: O(n)

---

## 2. `02_count_vowels_consonants.py`

### Problem
Count how many vowels and consonants appear in a string while ignoring spaces, digits, and special characters.

### Implementation details
- The input string is captured from the user.
- `filter(str.isalpha, str_input)` keeps only alphabetic characters.
- `.lower()` converts everything to lowercase so uppercase and lowercase are handled consistently.
- A loop iterates through each character.
- If the character is in the string `"aeiou"`, it is counted as a vowel; otherwise it is counted as a consonant.

### Example
```python
Enter a string to calculate the number of vowels and consonants := Hello World
Cleaned string is := helloworld
Vowels: 3, Consonants: 7
```

### Why this works
The program normalizes the input and removes non-letter characters before counting. This ensures the result reflects only the alphabetic content in the string.

### Time complexity
- Time: O(n)
- Space: O(n)

---

## 3. `03_largest_number.py`

### Problem
Find the largest number in a list without using Python's built-in `max()` function.

### Implementation details
- The user enters several numbers separated by spaces.
- `map(int, input().split())` converts the entries into integers.
- The list is sorted in ascending order.
- The last element of the sorted list is the largest number.

### Example
```python
Enter a list of numbers to find largest number := 12 45 7 89 23
Larges number from list is : 89
```

### Why this works
Sorting arranges the elements in order. After sorting, the maximum value will always be at the end of the list.

### Time complexity
- Time: O(n log n) due to sorting
- Space: O(n)

---

## 4. `04_remove_duplicates.py`

### Problem
Remove duplicate entries from a list while preserving the original order of the remaining elements.

### Implementation details
- The user provides a list of integers.
- The program iterates through each number.
- It checks whether the current value already exists in a new list called `final_lst`.
- If the number is not present, it is appended.
- This preserves the first appearance order while eliminating duplicates.

### Example
```python
Enter a list of numbers to remove duplicates := 1 2 2 3 1 4
List after removing duplicates is : [1, 2, 3, 4]
```

### Why this works
The program keeps only the first time each element appears. Because it checks membership before appending, duplicate values are skipped while the original sequence remains intact.

### Time complexity
- Time: O(n^2) in this implementation because membership checks in a list are linear
- Space: O(n)

---

## 5. `05_character_frequency.py`

### Problem
Count how many times each character occurs in a string and store the result in a dictionary.

### Implementation details
- The input is converted to lowercase so uppercase and lowercase letters are treated the same.
- Spaces are ignored.
- The program loops through each character in the string.
- For every character, it uses `str_input.count(ch)` to count occurrences.
- The result is stored in a dictionary where the key is the character and the value is the frequency.

### Example
```python
Enter a string to count the frequency of each character := Python
Frequency of each character in the string is := {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
```

### Why this works
A dictionary is ideal for storing paired data: a character and its count. Looping through the string and updating the dictionary makes frequency tracking straightforward and readable.

### Time complexity
- Time: O(n^2) when using `count()` inside the loop
- Space: O(n)

---

## Learning Goals for Day 02

By the end of this day, you should be able to:
- manipulate strings using slicing and filtering
- work with lists and dictionaries effectively
- count and compare values logically
- preserve order while removing repeated data
- build practical problem-solving patterns used in coding interviews

## Running the Scripts

From the repository root, use any of the following commands:

```bash
python "day 02/01_reverse_string.py"
python "day 02/02_count_vowels_consonants.py"
python "day 02/03_largest_number.py"
python "day 02/04_remove_duplicates.py"
python "day 02/05_character_frequency.py"
```

---

These exercises focus on common Python patterns for transforming data, counting values, and making code both clear and efficient.
