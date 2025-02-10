# in
# not in
# and 


word = "apple"

letter = input("guess a letter")
# can be: in / not in
if letter in word:
    print(f"there is a {letter}")
else:
    print(f"there is no {letter}")