# Functions
def computepay(h, r):
    if h>40:
        i=h-40
        t1=i*r*1.5
        t2=40*r
        total=t1+t2
    else:
        total=h*r
    return total
  
h=float(input("Enter Hours:"))
r=float(input('Enter rate:'))
        
p= computepay(h, r)
print("Pay", p)
