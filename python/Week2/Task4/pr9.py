"""
Convert Character Matrix to single String using string comprehension.
Example 1:

Input:

[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
Output:

campux is best channel

"""
l=[['c','a','m','p','u','x'],['i','s'],['b','e','s','t'],['c','h','a','n','n','e','l']]
output=''
for i in l:
    tmp=''.join(i)
    output+=' '
    output=output+tmp
print(output)    