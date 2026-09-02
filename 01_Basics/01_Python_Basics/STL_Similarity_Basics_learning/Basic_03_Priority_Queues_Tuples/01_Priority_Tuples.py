#the first item in the tuple can represent priority and if it's the same it goes to the second item
#(priority,value)
import heapq

heap=[]
heapq.heappush(heap,(2,"Task C"))
heapq.heappush(heap,(2,"Task B"))
heapq.heappush(heap,(3,"Task D"))
heapq.heappush(heap,(1,"Task A"))

print(heapq.heappop(heap))
print(heapq.heappop(heap))