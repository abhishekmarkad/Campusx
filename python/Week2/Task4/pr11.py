"""
Write a program that can perform union operation on 2 lists
Example:

Input:

[1,2,3,4,5,1]
[2,3,5,7,8]
Output:

[1,2,3,4,5,7,8]

"""

l1=[int(i) for i in input().split(' ')]
l2=[int(i) for i in input().split(' ')]

output=[]
for i in l1:
    if(i in output):
        continue
    else:
        output.append(i)
for i in l2:
    if( i in output):
        continue
    else:
        output.append(i)
print(output)        