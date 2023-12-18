"""
Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
Input:

hel123O4every093

Output:
22
"""
s=input('enter a alpha numeric string')
sum=0
n=0
for i in s:
    if('0'<=i and '9'>=i):
        sum+=int(i)
        n+=1
print('sum=',sum)
if(n!=0):
 print('avg=',sum/n)  
else:
   print('no number found')
          

