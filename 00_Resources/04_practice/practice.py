
array=[25,10,5,1]
n=int(input())
cnt=0
for i in array:
    m=n//i
    n=n-i*m
    cnt +=m
print(cnt)