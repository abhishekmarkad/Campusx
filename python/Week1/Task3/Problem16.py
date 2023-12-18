"""
Problem 16: Check whether the string is Symmetrical.
Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

Example 1:

Input

khokho
Output

The entered string is symmetrical
"""

s=input('enter a alphnumeric string')
a=s[:len(s)//2+1]
b=s[len(s)//2+1:]

if(a==b):
    print('string is symetric string')
else:
    print('string is not symetric')    