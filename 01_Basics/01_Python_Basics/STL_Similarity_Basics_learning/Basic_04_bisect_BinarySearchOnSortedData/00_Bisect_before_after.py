import bisect

arr=[1,2,3,4,4,5,6,7,8,9]

#before all repetitions of 4 comes
print(bisect.bisect_left(arr,4)) #bisect_left() finds the position where the target could be inserted before existing equal values.
#after all repetitons of 4 occurs
print(bisect.bisect_right(arr,4)) #bisect_right() finds the position where the target could be inserted after existing equal values.
