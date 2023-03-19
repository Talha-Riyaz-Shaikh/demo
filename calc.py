#calculator
n1= int()
n2= int()
n1= input ("Enter the 1st number:  ")
op= input ("Please enter the operator:  ")
n2= input ("Enter the 2nd number:  " )
if op == "+":
 print( int(n1) + int(n2) )
elif op== "-": 
 print( int(n1) - int(n2) )
elif op=="*":
 print( int(n1) * int(n2) )
else: print(int (n1) / int (n2))