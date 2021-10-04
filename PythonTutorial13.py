# Q -> Given a list swap the values of start and end

# myList = [1,2,3,4,5];
# [5,2,3,4,1]
# temp = myList[-1];
# myList[-1] = myList[0]
# myList[0] = temp;
# print(myList);

# Python program to swap two elements in a list

# def swap(myList,start,end):
#     temp = myList[start];
#     myList[start] = myList[end]
#     myList[end] = temp;
#     print(myList)

# swap(myList,2,4)
# swap(myList,3,2)
# swap(myList,0,3)

list1 = [1,2,32,451,5,531,231,5,1]
# find the max value out of list
# inbuild ways of find max/min in a list
# print(max(list1))
# print(min(list1))

def max(list1):
    maxValue = 0
    for num in list1:
        if num > maxValue:
            maxValue = num
    print(maxValue)

# max(list1)

# HW -> 

num = 10;
num2 = 20;
# print(min(num,num2))

# write a function to convert miles per hour to kmph

def milesToKmph(miles):
    print(miles*3)

# milesToKmph(10)

# *
# **
# ***
# ****
# *****

def printPattern(n):
    for i in range(1,n):
        print(i * "*")

# printPattern(10);

def factorial(n):
    fact = 1;
    for num in range(1,n+1):
        fact = fact * num
    print(fact)

# factorial(10)

# myList = [1,1,2,2,3,3,4,4,5,5]
# [1,2,3,4,5]
# print(list(set(myList)))

# print("hello World")

# Assuming (name = “John Smith”), what does name[1] return?
name = "John Smith"
# print(name[1])
# print(name[-2])
# print(len(name))

# len = 0
# for word in name:
#     len += 1
# print(len)
# power of 10
# print(10 ** 3)

# Name 3 iterable objects in Python.
# list [] {} ()
# string
# set
# tuples

# Club Silo
# entry 18+
# koi 18-21 -> grant entry -> NO alcohol
# koi 21-39 -> enrty + alcochol
# 39+ -> No entry


def clubSilo(age):
    if age >= 18 and age <= 21:
        print("Entry Granted But No Alcohol")
    elif  age >= 21 and age <= 39:
        print("Entry Granted !! Enjoy")
    else:
        print("No Entry")

# clubSilo(17)
# clubSilo(19)
# clubSilo(26)

# What is the difference between local and global variables?

#  Write a Python program which accepts the radius of a circle from the user and compute the area. 

def areaOfCircle(r):
    print(3.14 * r * r)

# HW
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
# write a program to find the min value in an list
# Write a Python program to display the first and last colors from the following list color_list = ["Red","Green","White" ,"Black"]
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Write a Python program to print the calendar of a given month and year.# Note : Use 'calendar' module.
# Write a Python program to get the volume of a sphere with radius 6.
# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
# Write a Python program to count the number 4 in a given list [1,2,3,4,1,3,4,4,4]
# Write a Python program that will accept the base and height of a triangle and compute the area
# Write a Python program to display your details like name, age, address in three different lines
