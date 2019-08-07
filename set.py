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
thisset.update(["mango", "blackBerry", "coconut"])
print(thisset)
print(len(thisset))

# remoce item in set list
print("\n")
thisset.remove("mango")
print(thisset)

thisset.discard("apple")
print(thisset)

thisset.pop()
print(thisset)

thisset.clear()
print(thisset)

# del  key can not use becouse  ther r not  index

# constructor to make a set
print("\n")
thisset1 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset1)

# difficalt item
print("\n")
x = {1,4,2,3,4,5,15}
y = {1,5,6,4,2,5,9}

print(x.difference(y))
print(y.difference(x))


# Remove the items that exist in both sets
print("\n")
x.difference_update(y)
print(x)
y.difference_update(x)
print(y)

# difficalt item
print("\n")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.intersection(y))
print(y.intersection(x))

# Remove the items that is not present in both x, and set y:
print("\n")
x.intersection_update(y)
print(x)
y.intersection_update(x)
print(y)

# all data
print("\n")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# unmatch diffrent
print("\n")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# check item
print("\n")
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


# sub set
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#no set here
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
