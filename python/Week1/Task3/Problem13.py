"""
Problem 13:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
Given:

str1 = PyNaTive

Expected Output:

yaivePNT

"""
s=input('enter your string')

ans=''

for i in s:
    if 'a'<=i and 'z'>=i:
        ans+=i
for i in s:
    if 'A'<=i and 'Z'>=i:
        ans+=i 
print(ans)               