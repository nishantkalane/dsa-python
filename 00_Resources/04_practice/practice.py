n=5
p=5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print(p,end=" ")
    for j in range(i+1):
        print(p,end=" ")
    p -=1
    print()