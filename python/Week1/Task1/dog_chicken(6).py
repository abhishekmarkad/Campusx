"""
Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
"""
heads=int(input('Enter Number of Head Counts'))
legs=int(input('Enter Number of Leg Counts'))

dogs=None
chicken=None

'''
dogs+chicken=heads
4*dogs+2*chicken=legs
2*dogs+chicken=legs/2
  
 -dogs-chicken=-heads
2*dogs+chicken=legs/2
----------------------
dogs=(legs//2 -heads)

chicken=heads-dogs


'''
dogs=(legs//2 -heads)
chicken=heads-dogs

print('Coutns of Dogs is ',dogs)
print('Counts of chicken is',chicken)

