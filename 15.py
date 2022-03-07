a=float(input("enter the first side of triangle"))
b=float(input("enter the second side of triangle"))
c=float(input("enter the third side of triangle"))
if(a+b>=c and b+c>=a and c+a>=b):
  print("valid")
else:
  print("invalid")
