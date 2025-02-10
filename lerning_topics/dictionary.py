
capitals = {"usa":"washington",
           "ukraine":"kiyev",
           "china":"beiging"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("usa"))
# capitals.update({"usa":"washington dc"})
# capitals.pop("usa")

# will remove the latest
# capitals.popitem()

# capitals.clear()

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(f"{key}: {value}")