a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
def gcd(a,b):
  if a==0 or b==0:
    return 0
  if a==b:
    return a
  if a>b:
    return gcd(a-b,b)
  return gcd(a,b-a)
def lcm(a,b):
  return a*b/gcd(a,b)
print("LCM of",a,"and",b,"is:",int(lcm(a,b)))
