"""
Problem 12: Append second string in the middle of first string
Input:

campusx
data
Output:

camdatapusx
"""

f=input('enter first string')
s=input('enter second string')

ans=f[:len(f)//2+1]+s+f[len(f)//2+1:]
print('your answer ',ans)