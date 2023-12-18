"""
Problem 7 - Reverse a given integer number.
"""
n=(input('Enter a Number'))

rev_n=''
l=len(n)
n=int(n)
while n>0:
    last_digit=n%10
    print(last_digit)
    rev_n+=str(last_digit)
    n=n//10
print('reverse of the number is',int(rev_n))  
print(str(0))  