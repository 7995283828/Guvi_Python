n=int(input("Enter the N value:"))
n1=0
n2=1
count=0
while count < n:
       print(n2,end=' ')
       sum = n1 + n2
       n1 = n2
       n2 = sum
       count += 1
