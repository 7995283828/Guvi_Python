a=input("Enter any string:")
def reverse(a):
  str = ""
  for i in a:
    str = i + str
  return str
b=reverse(a)
if a==b:
  print("Yes")
else:
  print("No")
