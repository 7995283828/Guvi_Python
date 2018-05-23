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
gcd(a,b)
print("GCD of" ,a ,"and", b, "is:",gcd(a,b))
