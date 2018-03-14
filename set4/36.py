symbols = "~`!@#$%^&*()_-+={}[]:;',.<>/?-+"
a=input("Enter the String:")
count=0
for i in a:
  if i in symbols:
    count+=1
print(count)
