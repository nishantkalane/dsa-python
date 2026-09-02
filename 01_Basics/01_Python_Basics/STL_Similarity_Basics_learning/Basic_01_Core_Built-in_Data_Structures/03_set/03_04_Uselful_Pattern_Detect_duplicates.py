nums={1,2,3,4,5,6,6,6,7,3,4}

def detect_duplicates(nums):
    return len(nums) != len(set(nums))

print(detect_duplicates(nums))