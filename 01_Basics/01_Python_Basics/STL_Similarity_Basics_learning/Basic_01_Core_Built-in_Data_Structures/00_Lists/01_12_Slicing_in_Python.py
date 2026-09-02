#let's understand slicing properly:

arr=[0,1,2,3,4,5]

#Remember:
#arr[start:stop:step]
#stop is excluded
n1=arr[1:4]
print(n1)
n2=arr[:3]
print(n2)
n3=arr[3:]
print(n3)
n4=arr[::2]
print(n4)
n5=arr[::-1]
print(n5)