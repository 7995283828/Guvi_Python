a=input("Enter any string:")
l=list(a)
b=[]
for i in l:
  if not i in b:
    b.append(i)
if len(b)==len(l):
  print("Yes")
else:
  print("No")
