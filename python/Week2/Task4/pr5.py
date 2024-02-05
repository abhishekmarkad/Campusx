"""

You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.

e. Say given list is [2,4,6,10,1] resultant list will be [22,20,16,10,23].

For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

like wise for all other elememts.

[2,4,6,10,1]-->[22,20,16,10,23]
"""
list1=[int(i)  for i in input().split(' ')]
output_list=[]
for i in range(len(list1)):
    sum=0
    for j in range(len(list1)):
        if(list1[j]>=list1[i]):
            sum+=list1[j]
    output_list.append(sum)        
print(output_list)