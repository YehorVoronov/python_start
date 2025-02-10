# can be set {} or tupple ()
fruit =  ["apple", "orange", "pinaple"]
vegetables = ["paper", "carrot"]
meats = ["pork", "chicken", "fish"]

groceries =[fruit, vegetables, meats]

# print(groceries[-1][0])

for collections in groceries:
    for item in collections:
        # instead of next line end= annd just space
        print(item, end=" ")
    print("")