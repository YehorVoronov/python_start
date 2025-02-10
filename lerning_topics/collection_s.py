# 2:23:09

# collection - single "varuable" used to store multiple values
#  List = [] ordered and changeable. Duplicates ok
#  Set = {} unordered and immutable, but Add/Remove OK, no duplicates
#  Tuple = () ordered and unchangeable. Duplicates OK,  faster


fruits = ["apple", "orange", "banana", "pineapple", "banana",]
# print(len(fruits))
# print(dir(fruits))
# print(help(fruits))
# print(fruits[::-1])

fruits[0] = "lemon"

fruits.append("addToTheEnd")
fruits.remove("orange")
fruits.insert(2,"coconut")
fruits.sort()
fruits.reverse()
# delete all the elements 
# fruits.clear()

print(fruits.index("addToTheEnd"))
print(fruits.count("banana"))

for fruit in fruits:
    print(fruit)

#2:32:51 

fruitsSet = {"apple", "orange", "banana", "pineapple", "banana",}

print(fruits)
print(fruitsSet)

# display atributes and methods of a set
# print(dir(fruitsSet))
# show scriptions of the method
# print(help(fruitsSet))

print("orange" in fruitsSet)

fruitsSet.add("something")
fruitsSet.remove("something")
# remove first element
fruitsSet.pop()
# delete all
fruitsSet.clear()


fruitsTuple = ("apple", "orange", "banana", "pineapple", "banana")
# dir, help, print("apple" in fruitsTuple), len(), .index("apple"), .count("apple")
