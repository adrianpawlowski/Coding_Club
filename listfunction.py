# Lists Function
myList = [ "One", "Two", "Three", "Four" ]
print(mylist)

# List Length
print(len(mylist))

# Append Value to List
mylist.append("Five")
print(mylist)
print(len(mylist))

# Insert Value to List
mylist.insert(0, "Zero")
print(mylist)
print(len(mylist))

# Combine Lists
secList = [ "Six", "Seven", "Eight", "Nine" ]
mylist.extend(secList)
print(mylist)
print(len(mylist))

# Removing Value from List

# Remove By Name
mylist.remove("Nine")
print(mylist)
print(len(mylist))

# Remove by Index
mylist.remove(7)
print(mylist)
print(len(mylist))

