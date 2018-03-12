n=int(input("Enter the n value:"))
a=int(input("Enter the a value:"))
d=int(input("Enter the d value:"))
sum = 0
for i in range(0,n):
  sum+= a
  a+= d
  i = i + 1
print(sum)
