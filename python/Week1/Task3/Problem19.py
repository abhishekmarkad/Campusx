"""
Problem 19: Word location in String.
Statement: Find a location of a word in a given sentence.

Example 1:

Input:

Sentence: We can learn data science through campusx mentorship program.

word: campusx
"""
sentence=input('enter your sentence')
word=input('enter the word')

print('location of the provided word in sentence ',sentence.find(word))