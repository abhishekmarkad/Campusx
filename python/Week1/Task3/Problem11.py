"""
Problem 11: Create Short Form from initial character
Given a string create short form ofthe string from Initial character. Short form should be capitalised.

Example:

Input:

Data science mentorship program
Output:

DSMP
"""
s=input('enter your string')
ans=''
for i in s.split():
    ans+=i[0].capitalize()

print(ans)
