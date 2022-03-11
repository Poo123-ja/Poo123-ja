cp=float(input("enter the cost price:"))
sp=float(input("enter the selling price:"))
if(sp==cp):
  print("No profit and loss")
else:
  if(sp>cp):
    print("The profit is",sp-cp)
  else:
    print("The loss is",cp-sp)
