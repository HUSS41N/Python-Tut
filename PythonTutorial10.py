# loops
myList = [1,2,3,4,5,6,7,8,9,10];

# this is very tideous for larger lists
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])
# print(myList[5])
# print(myList[6])

# for loop
# this process is known as iteration
# number of iteration is equls to length of the list
# for listItem in myList:
#     print(listItem)

# for i in myList:
#     print(i)

# for sania in myList:
#     print(sania)

# Q1 how to find lnegth of an array?
# eg [] = 0
# eg [1,2,3] = 3
# eg [1,2...n] = n

# length = 0;
# for item in myList:
#     length = length + 1;
# print(length)

# alternate way
# print(len(myList))

# Q2 print all the numbers btewwne 1 and n;

# n = int(input("Enter a value of n"))

# for number in range(1,n+1):
#     print(number)


# HOMEWORK
# q. print all the numbers which are divisble by 3 in range of 100;

# for num in range(1,101):
#     if(num % 3 == 0):
#         print(num)

# q. print all the even numbers in range of 200;

# for num in range(1,201):
#     if(num % 2 == 0):
#         print(num)

# q. pahada

# n = int(input("Enter a number"))
# for num in range(1,11):
#     print(num * n)

# khud krna h
# write a fizzbuzz upto 100;

# While loop
# syntax
# while true:
    # exciecute body
# num = 1;
# while num < 100:
#     print(num)
#     num = num + 1;


# while loop ka use kr k list k items print krne hue toh

# i = 0;
# while(i<len(myList)):
#     print(myList[i])
#     i = i+1;

for _ in range(1,101):
    print(_)
