p=int(input("enter the physics marks"))
c=int(input("enter the chemistry marks"))
m=int(input("enter the maths marks"))
b=int(input("enter the biology marks"))
c=int(input("enter the computer marks"))
total=p+c+m+b+c
print("total",p+c+m+b+c)
per=(total/500)*100
print("per is",per)
if(per>=90):
  print('A")
elif(per>=80):
  print("B")
elif(per>=70):
  print("C")
elif(per>=60):
  print("D")
elif(per>=40):
  print("E")
else:
  print("F")
