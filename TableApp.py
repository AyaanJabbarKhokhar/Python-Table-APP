a = int(input("Tell a Number For Table: "))
for i in range(1,11):
  print(i,"x",a,"=",i*a)

if a == 0:
  print("Invalid Number")
