import pandas as pd
l=[]
b=int(input("Enter Number of Elements:"))
for i in range(1,b+1):
    c=int(input(" "))
    l.append(c)
series = pd.Series(l)
print(series)
