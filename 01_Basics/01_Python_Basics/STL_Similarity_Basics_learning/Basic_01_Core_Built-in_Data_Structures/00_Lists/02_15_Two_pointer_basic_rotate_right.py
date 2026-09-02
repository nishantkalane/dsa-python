nums =[1,2,3,4,5]

def rotate_right(arr,k):
    k %=len(arr)

    return arr[-k:] + arr[:-k]

k=2
print(rotate_right(nums,k))