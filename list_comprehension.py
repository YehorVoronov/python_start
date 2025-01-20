# 4:46:00
# list comprehension = a concise way to create lists in python
# [expression for value in iterable if condition]

# doubles = []

# # bad approach
# for x in range(1,11):
#     doubles.append(x*2)

# print(doubles)



doubles = [x*2 for x in range(1,11)]