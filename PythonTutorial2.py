# list / array 
# a = 1;
# b = 2;
# c = 3;
# print(a)

nums = [1,2,3,4,5,6]
# indexing
# print(nums[2])
# slicing 
# print(nums[2:5])
# reverse
# print(nums[::-1])

# appending
# append will insert the provided value at last
nums.append(7)
nums.append(8)
nums.append(9)
# python lists are type independent
nums.append("TEN")
nums.append(True)
nums.append([1,2,3])
# print(nums)
# pop
# pop will remove the last element from the list
nums.pop();
nums.pop();
nums.pop();
# print(nums)

myList = [3414,4514,532,1,32,5,1,6,0]
# Sort a list
# sort
myList.sort();
# print(myList);

# decending order sort
myList.sort(reverse=True)
# print(myList)


names = ["Yatin","sania","akeel sir"]
# inserting at a particular index
# sytant list.insert(index,value)
names.insert(1,"Hussain")
names.insert(0,"Neha")
names.insert(2,"Shaishta")

# deleting at particular index
# just pass index to pop
names.pop(3)
print(names)
