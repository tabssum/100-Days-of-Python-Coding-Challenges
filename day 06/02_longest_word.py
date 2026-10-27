"""
Find the longest word in a sentence

Input: "Python programming is very interesting"

Expected output: "programming"

"""

# Online Python compiler (interpreter)
# Write and run Python online using this editor.


sentence=input("Enter a sentence a to find its longest word:= ")

words=sentence.split()

max_length_word=""

for word in words:
  if len(word)>len(max_length_word):
    max_length_word=word

print(f"Max length word in the {sentence} is := {max_length_word}")