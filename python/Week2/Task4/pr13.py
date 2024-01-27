"""
Write a list comprehension to print the following matrix
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
"""
l=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]

[print(second_ind) for first_ind in l for second_ind in first_ind]