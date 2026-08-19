# Append/pop from the end are O(1),
# inserting/removing at the front or middle is  O(n) because everything shifts.

#array or vector == Lists in python:

nums=[1,3,4,2,5,2,6,7]

#print a element
print("O(1)--direct indexing")
print(nums[2])
print()

#Add
print("O(1)-- Adds at the end")
nums.append(8) #
print(nums)
print()

#Removes
print("O(1)--removes last element")
nums.pop() #
print(nums)
print()


#Insert at 1st index
print("O(n) elements must shift right")
nums.insert(0,100) #elements must shift right
print(nums)
print()

#remove by index
print("O(n) all elements must shift left as first element is poped up")
nums.pop(0)
print(nums)
print()

#remove by value--removes the number when it occurs for the first time
print("O(n)--search +shifting")
nums.remove(2)
print(nums)
print()

#search
print("O(n)--linear search")
print(2 in nums)
print()

#length
print("O(1)--store as metadata")
print(len(nums))
print()

#slicking
print("O(k)-- creates a new list of k elements")
print(nums[1:4])
print()
#Reverse
print("O(n)--creates a reversed copy")
print(nums[::-1])