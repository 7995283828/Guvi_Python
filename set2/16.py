num1=int(input("Enter starting range:"))
num2=int(input("Enter ending range:"))
for i in range(num1+1,num2):
  if i>1:
    for j in range(2,i):
        if(i%j==0):
          break
    else:
        print(i)
