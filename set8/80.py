a=int(input("Enter number:"))
b=''
while(a!=0):
	t=a%10
	if t%2!=0:
		b=b+' '+str(t)
	a=a//10
print(b[::-1])
