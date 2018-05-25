n=int(input("Enter n value:"))
k=int(input("Enter k value:"))
l=[]
for i in range(0,n):
  l.append(int(input()))
print(l)
l.sort()
print(l[k-1])
