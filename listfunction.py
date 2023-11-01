# Lists Function
mylist = [ "One", "Two", "Three", "Four" ]
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
mylist.remove("Seven")
print(mylist)
print(len(mylist))

# Accessing Elements in a List
value = mylist[0]
print(value)

mylist[0] = "Zero (Edited)"
value = mylist[0]

print(value)

#Function

def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))


fahr_to_celsius(75)


def calculate_average():
    total = 0
    for num in numbers:
         total+=num
         return total/len(numbers)


calculate_average(6,7,8,9,10,14,13)