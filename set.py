thisset = {"apple", "banana", "cherry"}
print(thisset)

# unordered and unindexed.
print("\n")
for x in thisset:
    print(x)

print("\n")
if "apple" in thisset:
    print("apple is here")

# check bool
print("\n")
print("banana" in thisset)

# add item in set list
print("\n")
thisset.add("orange")
print(thisset)

# update item in set list
print("\n")
thisset.update(["mango","blackBerry","coconut"])
print(thisset)
print(len(thisset))

# update item in set list
print("\n")
thisset.remove("mango")
print(thisset)