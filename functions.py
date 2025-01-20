mystr = "soMe string"
lengthOfString =  len(mystr)
findChar = mystr.find(" ")
find2Char = mystr.find("str")
findLastChar = mystr.rfind("s")

print(lengthOfString)
print(findChar)
print(find2Char)
print(findLastChar)
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())

digitStr = "121321"
# bc it has space will return false
alphaStr = "fdsmk fmd"

print(digitStr.isdigit())
print(alphaStr.isalpha())

phone = "+1-232-432-1112"
print(phone.count("-"))
print(phone.replace("-","-->"))

# it will show all the methods available
print(help(str))