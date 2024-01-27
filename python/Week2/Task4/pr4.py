"""
###`Problem 4:` Running Sum on list
Write a program to print a list after performing running sum on it.

i.e:

`Input:`
```
list1 = [1,2,3,4,5,6]
```
`Output:`
```
[1,3,6,10,15,21]

"""
list1=[int(i) for i in input().split(' ')]

output_list=[]
sum=0
for i in range(len(list1)):
    sum+=list1[i]
    output_list.append(sum)
print(output_list)    
    