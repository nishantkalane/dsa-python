from collections import Counter

arr = [1,2,2,3,4,1,1,2,2,1,3,5,6,7,4,3]

freq = Counter(arr)


print(freq[2])
print(freq[7])

# TC = O(n)
# SC = O(n)