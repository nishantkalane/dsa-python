#we can get max heap by inserting the values as negative
import heapq

nums=[1,2,3,4,5,6,7,8,9]
num=[]
for x in nums:
    heapq.heappush(num,-x)

largest= -heapq.heappop(num)
print(largest)