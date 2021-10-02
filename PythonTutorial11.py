# functions
# complete block of code

# def nameOfFunction():
    # body

# defining a function
def printNumbers():
    for i in range(1,11):
        print(i)

# call function to execute function
# printNumbers();

def hello():
    print("Hello world")
    print("Hello world")
    print("Hello world")

# hello();

def sania_is_a_legend():
    print("Sania ka pyar sachha h ! She is true aashiq")

# sania_is_a_legend();

# fizzbuzz
# 1-100
# 3 - fizz
# 5 - buzz
# 3 and 5 fizzbuzz

def fizzBuzz():
    for num in range(1,101):
        if num % 15 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# fizzBuzz();

# functions parameters
# optional things we pass to functions
# optional parameters at the time of defining fucntion is knwon as parameters
def wishMeBirthday(name):
    print("Happy Birthday " + name)

# wishMeBirthday("Sania")
# wishMeBirthday("Neha")
# wishMeBirthday("Shaista")

def ageCalculator(age):
    print(2021 - age)

# when we call the function with the value the value is known as argument
# ageCalculator(1998)
# ageCalculator(1994)
# ageCalculator(1999)
# ageCalculator(2000)


num = 10;
def add10(num):
    num = num + 10
    print(num)

# add10(num);
# print(num)


# default arguments/parameteres

def say_hello(name = "Sania"):
    print("Hello " + name)

# say_hello("Neha")
# say_hello("Hussain")
# say_hello()

# multiple parameters
# def happyBirthday(name,age):
#     print("Happy Birthday " + name + " Now you are " + str(age) + " years old" )

def happyBirthday(name,age):
    print(f"Happy birthday {name} Now you are {str(age)} years old")

# happyBirthday("Sania",22)

# 1. Write a Python function to sum all the numbers in a list.
# 2. Write a Python function to multiply all the numbers in a list.
# 3. Write a Python program to reverse a string.
# 4. Write a python program to find if the string is a palindrom. string == reverse(String) eg "racecar" "aba"
# 5 Write a Python program to print the even numbers from a given list
    # Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Expected Result : [2, 4, 6, 8]
# 2. Write a Python function to multiply all the numbers in a list.
myList = [1,2,3,4,5]

ans = 1;

def multiply(myList,ans):
    for num in myList:
        ans = ans * num;
    print(ans)

# multiply(myList,ans);

# 4. Write a python program to find if the string is a palindrom. string == reverse(String) eg "racecar" "aba"

def palindrome(word):
    if word == word[::-1]:
        print("Word is a palindrome")
    else:
        print("Not a palindrome")

# palindrome("racecar")
