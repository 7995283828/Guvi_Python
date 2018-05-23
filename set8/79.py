import math
def perfectsqr(x):
  sr = math.sqrt(x)
  return((sr-math.floor(sr))==0)
a=int(input("1st number:"))
b=int(input("2nd number:"))
x=a*b
if (perfectsqr(x)):
  print("Yes")
else:
  print("No")
