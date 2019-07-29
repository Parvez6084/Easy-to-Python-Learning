

b = """ In Operating Systems,
    Segmentation is a memory management technique in which,
    the memory is divided into the variable size parts. 
    Each part is known as segment which can be allocated to a process. 
    The details about each segment are stored in a table called as segment table."""

print(b)
print("\n")


# String  Arrays
a = "Parvez Ahmed"

print(a)
print(a[0])
print(a[7])


# in a Arrays start point and end point
print("\n")
print(a[3:10])

# in a String  divided
print("\n")
e = "12:26:29"
print(e.split( ":" ))
print(e.split( ":" )[2])


# in a String  space remove
print("\n")
print(a.strip())

# in a String size
print(len(a))

# in a String  lower case and upper case
print("\n")
print(a.lower())
print(a.upper())

c = "parvez"
d = "Ahmed"
print(c.islower())
print(d.isupper())

# replace string
print("\n")
print(a)
print(a.replace("P","N"))
print(a.replace("Ahmed","Khan"))
print(a.replace(a[2],"F"))
print(a.replace(a[2:6],"flatter"))

