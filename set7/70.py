a=int(input("Enter any number:"))
for i in range(0,a):
  num=2**i
  if num>a:
    print(num)
    break
if a==2:
  print("4")
elif a==1 or a==0:
  print("2")
