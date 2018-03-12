a=0
b=0
c, d = [int(x) for x in input("Enter 1st Time(hrs:min):").split()]
e, f = [int(y) for y in input("Enter 2nd Time(hrs:min):").split()]
a=c-e
b=d-f
print("%d %d"%(a,b))
