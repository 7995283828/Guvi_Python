n=int(input("Enter the N value:"))
a=0
b=1
count=0
while count < n:
       print(b,end=' ')
       sum = a + b
       a = b
       b = sum
       count += 1
