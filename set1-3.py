ch = input("Input a character:")

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("It is a vowel.")
elif(int(ch)>=0 and int(ch)<=9):
        print("It is a number")
else:
    print("It is a consonant.")
