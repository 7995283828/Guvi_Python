lst=[]
b=10
for i in range(1,b+1):
    c=int(input(" "))
    lst.append(c)
lst.sort()
print("Largest Element is:",lst[b-1])
