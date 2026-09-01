from collections import deque

#deque means: double ended queue--It allows you to efficiently add / remove from both ends.

q=deque()

q.append(20) #add to right
q.append(30) # add to right
print(q)

q.appendleft(10) #add to left
print(q)

q.pop() #remove from right
print(q)
q.popleft() #remove from left
print(q)

#we could have used a list but we shouldn't because poping(0)th element will make all of them to shift inlist and removing and shifting will cause O(n)