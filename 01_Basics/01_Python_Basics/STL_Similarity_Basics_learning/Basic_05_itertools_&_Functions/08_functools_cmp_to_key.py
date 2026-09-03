# cmp_to_key() let's Python's sorted() use an old style comparison function
from functools import cmp_to_key

def compare(a,b):
    return a-b
nums=[3,2,1]

print(sorted(nums))


print(sorted(nums, key=cmp_to_key(compare)))