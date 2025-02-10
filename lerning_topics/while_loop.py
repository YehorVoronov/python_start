
number= 1

while  number<=5:
    print("true")
    number = number+2
    if number == 4: 
        break
    
print("loop is done")


num = int(input("enter a number between 1-10 "))

while num<1 or num >10:
    print("wrong number try again")
    num = int(input("enter a number between 1-10 "))
print(f"your number is {num}")

