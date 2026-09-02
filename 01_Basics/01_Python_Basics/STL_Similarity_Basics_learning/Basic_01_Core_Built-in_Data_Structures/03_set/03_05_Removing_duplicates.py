nums=[3,3,8,1,2,2,2,3,4,5,6,6,7]

unique=set(nums)
print(unique)
nums2=[3,3,8,1,2,2,2,3,4,5,6,6,7]
#to preserve the original insertion order use : dict.fromkeys()
n=list(dict.fromkeys(nums2))
print(n)