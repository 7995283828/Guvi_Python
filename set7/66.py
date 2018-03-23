a = int(input("Enter any number: "))
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")
