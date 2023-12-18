"""
Problem 13:Print all the Armstrong numbers in a given range.
Range will be provided by the user
Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.


"""
n1=int(input('enter lower limit'))
n2=int(input('enter Upper limit'))

for i in range(n1,n2+1):
    k=i
    sum=0
    while k>0:
        last_digit=k%10
        sum+=last_digit*last_digit*last_digit
        k=k//10
    if(sum==i):
        print(i,end=',')
            
