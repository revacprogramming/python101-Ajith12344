# Conditional Executi
hrs = input("Enter Hours:")
h = float(hrs)
r=float (input('Enter rate:')) 
if h>40:
    i=h-40
    t1=i*r*1.5
    t2=40*r
    total=t1+t2
    print(total) 
else:
    total=h*r
    print(total) 