#reverse an array
nums=[1,2,3,4,5] #we want the output to be [5,4,3,2,1]
#we want to modify the same list rather than creating another one\
print(nums)
def reverse_in_place(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]

        left +=1
        right -=1

    return arr



print(reverse_in_place(nums))