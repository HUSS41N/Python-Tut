
def say_hello(name):
    return f"Hello {name}"

# we must return the value from the function to assign it to someother vairable
# ans = say_hello("Hussain")
# print(ans[::-1])

nums = [1,2,3,4,5]
sum = 0

def sumOfList(nums,sum):
    for _ in nums:
        sum += _;
    return sum

sum = sumOfList(nums,sum)

def helperFunc(sum):
    print(f"Total sum is {sum}")

helperFunc(sum);

from random import randint, shuffle;
# from packageName import functionName
import datetime
import math

# myList = [1,2,3,4,5]
# print(myList)
# shuffle(myList)
# print(myList)
# shuffle(myList)
# print(myList)
# shuffle(myList)
# print(myList)
# shuffle(myList)
# print(myList)

# print(datetime.datetime.now())
# print(math.sqrt(4))
# print(math.factorial(10))


names = ["Neha","Shaista","Faisal","Aadil"]

index = randint(0,3)

print(names[index])       
