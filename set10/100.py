a=int(input("Enter the number:"))
b=1
while a>0:
  c=a%10
  b*=c
  a//=10
print(b)
