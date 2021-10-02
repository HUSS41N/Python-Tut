
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
