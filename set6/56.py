a=input("Enter:")
set1=0
set2=0
for i in range(0,len(a)):
  if 'a'<=a[i]<='z':
    set1=1
    break
for i in range(0,len(a)):
  if '0'<=a[i]<='9':
    set2=1
    break
if set1==1 and set2==1:
  print("Yes")
else:
  print("No")
