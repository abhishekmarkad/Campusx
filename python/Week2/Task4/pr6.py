"""
Find list of common unique items from two list. and show in increasing order
Input

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
Output:

[34, 67, 89]
"""
num1=[int(i) for i in input().split()]
num2=[int(i) for i in input().split()]

result=[]

for i in range(len(num1)):
    if(num1[i] in result):
        continue
    is_common=False
    for j in range(len(num2)):
        if(num1[i]==num2[j]):
            is_common=True
    if(is_common):
        result.append(num1[i])        

# to take common from num2
for i in range(len(num2)):
    if(num2[i] in result):
        continue
    is_common=False
    for j in range(len(num1)):
        if(num2[i]==num1[j]):
            is_common=True
    if(is_common):
        result.append(num2[i]) 
result.sort()
print(result)        
        
