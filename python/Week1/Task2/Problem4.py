"""
Problem 4: Write a menu-driven program -
cm to ft
km to miles
USD to INR
exit

"""

op=int(input("""Enter as per Your need\n
             1 cm to ft\n
             2 km to miles\n
             3 USD to INR\n
             4 exit
             """))

if(op==1):
    cm=float(input('enter cms'))
    #1cm = 0.0328084 ft
    fts=cm*0.0328084
    print(cm," cm is equal to ",fts," ft")
elif(op==2):
 km=float(input('enter kilometers'))
 #1km = 0.621371 miles
 miles=km* 0.621371
 print(km,' km is equl to ',miles," miles")
elif(op==3):
   usd=float(input('enter USD'))
   #1usd- 83.04 (at this moment [15/12/2023])
   ruppes=usd*83.04
   print(usd,' USD is equal to ',ruppes,' Rs')
else:
   print('Hope you like it, any suggestion')
       

