"""
Problem 20: Write a program that can remove all the duplicate characters from a string. User will provide the input.
"""
s=input('enter your sentence')

ans=''
for i in s:
    if s.count(i)==1:
        ans+=i
print('ans =',ans)        

