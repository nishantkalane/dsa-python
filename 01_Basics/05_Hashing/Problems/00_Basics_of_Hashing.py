

size_of_array=int(input("Size of Array: "))
arr = list(map(int,input("Enter numbers separated by ',' ").split(",")))
print(arr)
ask_no = int(input())

#pre compute
hash_table =[0]*13
for i in range(len(arr)):
    print(i)
    print(arr[i])
    print(hash_table[arr[i]])
    hash_table[arr[i]] +=1

while ask_no != 0:
    # fetch
    number = int(input("Which number you want in check"))
    print(hash_table[number])
    ask_no -= 1
