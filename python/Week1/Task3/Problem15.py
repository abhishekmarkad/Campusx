"""
Problem 15: Removal of all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510
"""

s=input('enter a alpha numeric string')
ans=''

for i in s:
    if(i>='0' and '9'>=i):
        ans+=i

print('string after removing all the characters ',ans)
