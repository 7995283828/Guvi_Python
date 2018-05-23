a=input("Enter any string:")
l=list(a)
b=''
for i in l:
  if i.isnumeric():
    b+=i
print(b)
