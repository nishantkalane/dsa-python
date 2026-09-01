#counter is basically a dictionary specially designed for counting things

#instead of :
freq={}
for x in "banana":
    freq[x]=freq.get(x,0)+1

print(freq)

#we do
from collections import Counter
freq = Counter("My name is Nishant")
print(freq)

#Getting the most common .most_common(2) means give me the 2 most frequent elemts
print(freq.most_common(2))