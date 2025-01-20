age = input("what is your age?")


if not age.strip():
    print("you didn't print anything!")
elif int(age) <18:
    print("you're very yang")
elif int(age) > 45:
    print("you're 45+")    
elif int(age) >18:
    print("you're more than 18")
else:
    pass


response = input("do you agree? Y/N")
if response== "Y":
    print("you are agre")
elif response == "N":
    print("you are disagre")
else:
    print("answer does not match")