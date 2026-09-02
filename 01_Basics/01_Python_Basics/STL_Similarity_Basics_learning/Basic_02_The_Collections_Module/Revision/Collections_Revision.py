from collections import Counter

name= ("Nishant Kalane".lower())
#counter
print(Counter(name).most_common(2))
text="Hello"
print(text.count("e"))

from collections import defaultdict

words=["Ram", "Rajec", "Ansh", "Aniket", "Bablu", "Bansi", "Nish"]
groups= defaultdict(list)
print(groups)

for word in words:
    first=word[0]
    groups[first].append(word)
for key, value in groups.items():
    print(key,value)

from collections import deque

q= deque()
q.append(10)
q.append(20)
q.append(30)

print(q)
q.popleft()
print(q)
q.pop()
print(q)
q.appendleft(10)
print(q)