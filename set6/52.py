def switch_fun(argument):
    switcher = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
    }
    print(switcher.get(argument, "Number not in range"))
a=int(input("Enter number between 1 to 10:"))
switch_fun(a)
