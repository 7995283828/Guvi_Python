num1=int(input("Enter the starting range:"))
num2=int(input("Enter the ending range:"))
for i in range(num1+1,num2):
    if(i%2!=0):
        print(i)
