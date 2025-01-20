import math

anyNumber = 5

numberSquared = anyNumber **2

print(f"squared number of {anyNumber} : {numberSquared}")

remainder = anyNumber%2
print(f" remainder of {anyNumber} %2 : {remainder}")

floatNumber =3.14
print(f"rounded 3.14 (one digit) = {round(floatNumber,1)}")

negativeNumber = -4

print(f"absolute number of negative number : {abs(negativeNumber)}")

print(f"pow it is nummber times pow number (anyNumber*anyNumber 3 times) {pow(anyNumber,3)}")

x= 3
y =5
z = 20

print(f"max value {max(x,y ,z)}")
print(f"min value {min(x,y ,z)}")


piNumber = math.pi

print(f"pi number {piNumber}")
print(f"e number {math.e}")
print(f"sqrt of 9---> {math.sqrt(9)}")

#round up 
# math.ceil(x)
# round down
# math.floor(x)