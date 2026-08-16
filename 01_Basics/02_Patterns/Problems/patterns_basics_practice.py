#Printing some practice sets from notebook notes from notes section # Feel Free to skip this part

n =5
print("*")

print()

print("*"*n)

print()

for i in range(n):
    print("*")
print()

for i in range(n):
    print("*", end=" ")

print()
print()
for i in range(n):
    for j in range(n):
        print("*", end=" ")

print()
print()
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print()
print()

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
print()
print()

for i in range(n):
    for j in range(i,n):
        print("#", end=" ")
    print()
