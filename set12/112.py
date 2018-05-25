n=int(input("Enter N number:"))
k=int(input("Enter K value:"))
b=[]
for i in range(0,n):
  a=int(input())
  b.append(a)
if k in b:
  print("Yes")
else:
  print("No")
