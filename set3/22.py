a=[]
b=int(input("Enter Number of Elements:"))
for i in range(1,b+1):
    c=int(input(" "))
    a.append(c)
a.sort()
print("Largest Element is:",a[b-1])
