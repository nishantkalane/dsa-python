from collections import Counter
a=Counter("aabbaabbcd")
b=Counter("ababc")

print(a)
print(b)

print("add--wlement wise sum")
print(a+b)
print("sub--only positive diff")
print(a-b)
print("OR")
print(a | b)
print("Intersection count")
print(a & b)