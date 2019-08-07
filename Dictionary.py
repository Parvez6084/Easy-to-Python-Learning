userInfo = {
    "name": "Parvez",
    "age": "26",
    "post": "developer",
    "joinYear": 2019
}
print(userInfo)

# specific post
print("\n")
print(userInfo["post"])

x = userInfo.get("age")
print(x)

#  post value change
userInfo["age"]=27
print(userInfo)

# list one item
print("\n")
for x in userInfo:
    print(x)

# list item result
print("\n")
for x in userInfo:
    print(userInfo[x])

# list item result
print("\n")
for x in userInfo.values():
    print(x)

# list item result with key
print("\n")
for x,y in userInfo.items():
    print(x,y)

# list add item
print("\n")
userInfo["color"] = "Green"
print(userInfo)
# list re item
userInfo.pop("age")
print(userInfo)

userInfo.popitem()
print(userInfo)