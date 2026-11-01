arr = [ 2,3,2,1,2,1,4,5,4,5,4]
freq = {}

for num in arr :
    freq[num] = freq.get(num,0) + 1
print(freq.get(1))
print(freq.get(2,0))

#TC = O(n)
#SC= O(k) ( k number of distinct elements )