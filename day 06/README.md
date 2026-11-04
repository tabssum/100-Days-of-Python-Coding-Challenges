# Day 06: List and String Challenges

This folder contains exercises for working with list intersections, word lengths, list rotations, and consecutive-character compression. The implemented scripts use loops, list operations, string processing, and `itertools.groupby`.

## Files Included

### 1) `01_list_intersection.py`
**Problem:** Find the intersection of two lists without duplicates.

The file currently contains the problem statement and an example only; the solution has not been implemented yet.

**Expected example:** `[1, 2, 2, 3, 4]` and `[2, 3, 3, 5]` should produce `[2, 3]`.

### 2) `02_longest_word.py`
**Problem:** Find the longest word in a sentence.

**Implementation details:**
- Reads a sentence from the user and splits it into words with `split()`.
- Iterates over the words and tracks the longest one found so far.
- Prints the selected word. If multiple words share the maximum length, the first one is kept.

**Time complexity:** O(n), where n is the sentence length.  
**Space complexity:** O(n) for the list of words.

### 3) `03_rotate_list.py`
**Problem:** Rotate a list to the left by K positions.

**Implementation details:**
- Reads space-separated integers and a rotation count K.
- Builds a new list by appending elements starting at index K, then appending the first K elements.
- Prints both the original and rotated lists.

For the implementation to work as intended, K should be between 0 and the list length, inclusive. Values larger than the list length can cause an index error; negative values are not normalized.

**Time complexity:** O(n), where n is the number of list elements.  
**Space complexity:** O(n) for the rotated list.

### 4) `04_string_compression.py`
**Problem:** Compress a string by counting consecutive occurrences of each character.

**Implementation details:**
- Uses `itertools.groupby` to group adjacent identical characters.
- Counts each group and appends the character and its count to the output.
- Only consecutive repetitions are combined; separated runs of the same character are represented separately.

**Example:** `aaabbccccdaa` becomes `a3b2c4d1a2`.

**Time complexity:** O(n) for grouping and counting n input characters, excluding the cost of repeatedly concatenating the output string.  
**Space complexity:** O(n) for the compressed output and temporary group data.

## Summary

These exercises provide practice with:
- iterating over lists and tracking a best candidate
- rotating list elements into a new order
- processing consecutive character runs with `groupby`
- understanding an unfinished problem statement and the input constraints of a solution

## Running the Implemented Scripts

From the repository root, run:

```bash
python "day 06/02_longest_word.py"
python "day 06/03_rotate_list.py"
python "day 06/04_string_compression.py"
```

`01_list_intersection.py` is not runnable as a solution yet because it contains no implementation.
