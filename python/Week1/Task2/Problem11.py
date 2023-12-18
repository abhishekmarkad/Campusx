"""
Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.
"""
for i in range(1000,3001):
    k=i
    while i>0:
        last_digit=i%10
        if(last_digit%2==1):
            break
        i=i//10   
    else:
        print(k,end=' ')    
