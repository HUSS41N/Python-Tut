# Type conversion

# int
num = 10;
# print(type(num))
# name = 'x'
# print(type(name))

# int to float and float to int
# print(float(num))
num2 = 19.99
num3 = int(num2)
print(num3)


# name = "Neha"
# print(int(name))

stringNum = "1999"
print(int(stringNum))

num4 = 1998
s = str(num4)
print(type(s))

# given a list remove all the duplicate elements
# [1,2,3,1,1,2,2,3] = [1,2,3]
# hint convert list to set and set to list

# given a list count the number of 1's
# [0,1,0,1,1,1,0] => 4

# type conversion
# convert one data type into other
num = 10.77; #flot type 
# print(num)

# Syntax for type conversion nameofvaribale = typeToBechanged(varible we want to change)

# checking type
# print(type(num))

# int()
# print(int(num))

# age = 23
# ageFloat = float(age)
# print(ageFloat)

# cake = "1998"
# print(type(cake))
# # string to integer
# print(int(cake) + 2)

# given a list remove all the duplicate elements
# [1,2,3,1,1,2,2,3] = [1,2,3]
# hint convert list to set and set to list

# myList = [1,2,3,1,1,2,2,3]
# mySet = set(myList)
# myList = list(mySet)
# print(myList)

# given a list count the number of 1's
# [0,1,0,1,1,1,0] => 4

# myList = [0,1,0,1,1,1,0]
# # print(myList.count(1))

# myTuple = tuple(myList)
# print(myTuple.count(1));

# first intstace k liy hi kaam krega
myTuple = (1,2,4,3,4,5,6,4);
print(myTuple.index(4))
