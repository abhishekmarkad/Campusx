"""
Problem 17: Reverse words in a given String
Statement: We are given a string and we need to reverse words of a given string.

Example 1:

Input:

geeks quiz practice code
Output:

code practice quiz geeks
"""
s=input('enter a string')

a=s.split()
a=reversed(a)
print(' '.join(a))