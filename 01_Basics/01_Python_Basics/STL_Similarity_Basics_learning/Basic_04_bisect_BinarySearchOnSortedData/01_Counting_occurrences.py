import bisect

arr=[1,3,4,5,5,5,5,7,8,9,10] #sorted array

#how many  times an element occurs

left=bisect.bisect_left(arr,5)
right=bisect.bisect_right(arr,5)

print(right-left)
