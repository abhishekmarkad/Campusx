"""
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
Given List:

list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
Output:

[['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]

"""

list1=[i for i in input().split(' ')]
list2=[i for i in input().split(' ')]

final_list=[]
len1=len(list1)
len2=len(list2)

for i in range(max(len1,len2)):
    
    temp_list=[]
    if(i<len1):
        temp_list.append(list1[i])
    if(i<len2):
        temp_list.append(list2[i])
    final_list.append(temp_list)
print('Final list-->',final_list)            