# exception = An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)
# 1.try 2.except 3.finally

try:
    number = int(input("give the number"))
    print(1/number)
except ZeroDivisionError:
    print("should be different from 0") 
except ValueError:
    print("should be number")   
except Exception:
# for all error which will happen 
    print("error in my try catcch")
finally:
    # maybe close oppened files in try or something else
    print("it will work 100% no matter what")