# bisect.insort(arr,k) can be used to insert a k element in an arr without minding the sequence of array
import bisect

arr=[1,2,3,4,5,6,8,9,10]

bisect.insort(arr,7)
print(arr)