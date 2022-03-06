a=int(input("Enter the first side"))
b=int(input("Enter the second side"))
c=int(input("Enter the third side"))
if(a==b and b==c):
    print("Equilateral Triangle")
elif(a==b and b==c and c==a):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
