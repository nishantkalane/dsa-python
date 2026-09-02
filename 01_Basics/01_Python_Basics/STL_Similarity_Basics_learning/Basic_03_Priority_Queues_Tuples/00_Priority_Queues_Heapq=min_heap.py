#smallest element has the highest priority:
import heapq

h =[] #usually use python list to store the heap

heapq.heappush(h, 4) #the list behaves like  a heap
heapq.heappush(h,3)
heapq.heappush(h,5)
#remove smallest element
print(heapq.heappop(h)) #gives 3 even though 4 was inserted first , as 3 was the smallest

#converting a list into a heap
nums =[1,3,4,5,6,7,8,9,0,1,2,3,7]

heapq.heapify(nums) #heapify to convert a list into heap
print(heapq.heappop(nums))

#getting k smallest values : heapq.nsmallest(k,nums)

print(heapq.nsmallest(2,nums))
print(heapq.nlargest(2,nums))
