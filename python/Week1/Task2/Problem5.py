"""
Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
"""
first=0
second=1
print(0,end=' ')
print(1,end=' ')
for i in range(3,11):
    third=first+second
    print(third,end=' ')
    first=second
    second=third