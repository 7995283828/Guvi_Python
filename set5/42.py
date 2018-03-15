str1=input("Enter 1st string:")
str2=input("Enter 2nd string:")
if len(str1)>=len(str2) and max(str1)>=max(str2):
  print(str1)
else:
  print(str2)
