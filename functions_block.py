#  *args - allows your to pass multiple non-key arguments
#  **kwargs - allows your to pass multiple keyword-arguments



# def happy_birthday(name, age):
#     print(f"Happy {age} Birthday {name}!")
#     print("all the best")
#     print()

# happy_birthday("Tom", 20)
# happy_birthday("Roy", 30)


# def add_params(params):
#     total= 0 
#     for e in params:
#         total += e
#     return total


# print(add_params([1,4,6]))

# def create_name(first_name, last_name="defaultSurname"):
#     first_name = first_name.capitalize()
#     last_name = last_name.capitalize()
#     return first_name+ " " + last_name

# print(create_name("george", "andriano"))
# print(create_name("tom"))

# import time
# def count(end, start=0):
#     for x in range(start, end):        
#         print(x)
#         time.sleep(1)
#     print("done!")

# count(15, start = 1)    
    

# def add_args(*args):
#     total= 0 
#     for arg in args:
#         total = total+arg
#     return total

# print(add_args(2,3,5,6))

# def kwargs_function(**kwargs):
#     for key, val in kwargs.items():
#         print(f"key:{key}, val:{val} ")

# kwargs_function(name="don", age=23)  

def args_kwags(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for val in kwargs.values():
        print(val, end = " ")
    
    print()
    print(f"street number : {kwargs.get("street")}")

args_kwags("dr", "berg", "args", street="1", apt="30")