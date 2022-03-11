bs=int(input("enter the basic salary"))
if(bs<=10000):
  hra=(bs*20)/100
  da=(bs*80)/100
  gross salary=hra+da+bs
 elif(bs<=20000):
  hra=(bs*25)/100
  da=(bs*90)/100
  gross salary=hra+da+bs
 elif(bs>20000):
  hra=(bs*30)/100
  da=(bs*95)/100
  gross salary=hra+da+bs
 print("The gross salary is",gross salary)
