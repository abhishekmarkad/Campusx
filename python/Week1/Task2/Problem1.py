"""
Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - 
HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%
"""
ctc=float(input('Enter Your CTC (in lakhs)'))

InHand=None

if(ctc<=5):
    InHand=ctc
elif(ctc<=10):
    InHand=ctc*90/100     # 10% tax deducted , remaining 90%
elif(ctc<=20):
    InHand=ctc*80/100  # 20% tax deducted, remainin 80%
else:
    InHand=ctc*70/100 # 30 , remainng 70%

#HRA(10%), DA(5%), PF(3%)
InHand=InHand-18*ctc/100 # 18 (10+5+3) deducted of ctc

print('In hand Salary after deducting taxes ,HRA,DA and PF is ',InHand)
