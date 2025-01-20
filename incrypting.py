
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# ENCRYPT

plain_text = input("write your text")
cipher_text = ""

for i in plain_text:
    index = chars.index(i)
    cipher_text += key[index] 


print(f"original: {plain_text}")
print(f"encrypted: {cipher_text}")


# DECRYPT
new_cypher = input("give me sypher text")
decrypted = ""
for i in new_cypher:
    index = key.index(i)
    decrypted += chars[index] 


print(f"cipher_text: {new_cypher}")
print(f"decrypted: {decrypted}")