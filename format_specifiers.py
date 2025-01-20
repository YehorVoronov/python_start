#  format specifiers = {value:flags} format a value based on what flags are inserted
price1 = 3333.123124314
price2 = -9837.42
price3 = 12323.34

# print(f"price 1 is {price1:.2f}")
# print(f"price 2 is {price2:.3f}")
# print(f"price 3 is {price3:.2f}")

# # total 10 spaces for each value
# print(f"price 1 is {price1:<010}")
# print(f"price 2 is {price2:<010}")
# print(f"price 3 is {price3:<010}")

# #with + or - in it
# print(f"price 1 is {price1:+}")
# print(f"price 2 is {price2:+}")
# print(f"price 3 is {price3:+}")

# # to separate thousands add ,

# #with + or - in it
# print(f"price 1 is {price1:,}")
# print(f"price 2 is {price2:,}")
# print(f"price 3 is {price3:,}")


print(f"price 1 is {price1:+,.2f}")
print(f"price 2 is {price2:+,.2f}")
print(f"price 3 is {price3:+,.2f}")

#.(number)f = round to that many decimal places (fixed point)
#:(number) = allocate that many spaces
#:03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use plus sign to endicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator