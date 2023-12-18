"""
Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.
"""
n=None
nth=0
sum=0 
while n!=0:
    n=int(input('Enter new number'))
    sum+=n
    nth+=1
else:
    print('average',sum/nth)    

