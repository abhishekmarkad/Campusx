"""
Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number
"""
n=int(input('enter a decimal number'))
s=''
while n>0:
    rem=n%2
    s+=str(rem)
    n=n//2
s=s[::-1]    
print(s)
