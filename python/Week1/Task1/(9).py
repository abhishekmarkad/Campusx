"""
Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

input format a/b
"""

s=input('Enter a fraction (x/y)')
n=int(s.split('/')[0])
d=int(s.split('/')[1])
sum=n+d

print('sum of Numerator and denomitor is ', sum)