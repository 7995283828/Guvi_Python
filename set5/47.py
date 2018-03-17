n= int(input("Enter the number of inputs:"))
b=[]
print("Enter the numbers:")
for i in range(0,n):
  b.append(int(input()))
print(str(min(b))+" "+str(max(b)))
