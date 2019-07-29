
person = ["arif","parvez","mamun","zaker"]
print(person)
print(person[1])
print(len(person))

# list item change
print("\n")
person[2] = "rubel"
print(person)

# list item for loof
print("\n")

for x in person :
    print(x)


# list item search
print("\n")

if "mamun" in person :
    print("mamun is here")
else:
    print("mamun is not Found")


# list item data add
print("\n")

person.append("mamun")
person.insert(2,"sunny")
print(person)

#remove items from a list
print("\n")

person.remove("sunny")
print(person)

person.pop()
print(person)


del person [0]
print(person)


person.clear()
print(person)


#coppy a list
print("\n")

word = ["p",'f','i',2,98]
print(word)

copy_word = word.copy()
print(copy_word)

mylist =list(word)
print(mylist)

thislist = list(("apple", "banana", "cherry"))
print(thislist)

print("\n")
c = [1,2,8,6,9,4,3,5,9,5,5,74,4,9,5,3,5,5,]
print("this list 5 here in ",c.count(5)," time")


man = ["arif","parvez","mamun","zaker"]
selery = [18000,25000,26000,25000]

man.extend(selery)
print(man)
print(selery)

print("\n")
man.reverse()
print(man)


man1 = ["arif","parvez","mamun","zaker"]
print("\n")
man1.sort()
print("sort data are ")
print(man1)