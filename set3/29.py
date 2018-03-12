a=int(input("Enter time in minutes:"))
mins = a % 60
hrs = (a - mins)/ 60
print ("%d %d" % (hrs, mins))
