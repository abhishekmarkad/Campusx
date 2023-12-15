"""
swap two number taken from user without using 3rd variable
"""
num1=int(input('Enter Num1'))
num2=int(input('Enter num2'))

num1,num2=num2,num1
#there are many approaches but this one is simple
print('num1 =',num1)
print('num2 =',num2)