"""
Problem 18: Find uncommon words from two Strings.
Statement: Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

Example 1:

Input:

A = "apple banana mango" 
B = "banana fruits mango"
Output:

['apple', 'fruits']
"""
f=input('enter first string')
s=input('enter second string')

ans=[]
for i in f.split():
    if( i not in s):
        ans.append(i)
for i in s.split():
    if( i not in f):
        ans.append(i)        
print(ans)