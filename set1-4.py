ch = input("Enter a character: ")
if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print(ch, "is an Alphabet")
elif '0'<=ch<= '9':
    print("It is not an Alphabet")

else:
    print(ch, "Invalid input")
