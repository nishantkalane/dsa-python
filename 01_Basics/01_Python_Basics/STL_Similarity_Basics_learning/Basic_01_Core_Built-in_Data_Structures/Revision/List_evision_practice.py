nums =[10,20,30,40,50]

print(nums[0])
print(nums[-1])
nums[2]=100
print(nums)
nums.append(60)
print(nums)
nums.pop(5)
print(nums)
print(len(nums))

#slicing
nums2 = [1,2,3,4,5,6]

print(nums2[1:4])
print(nums2[:3])
print(nums2[3:])
print(nums2[::2])
print(nums2[-1::-1])

#loop
for index, value in enumerate(nums2): #enumerate is good to get both the index and value
    print(f"{index} -> {value}")


#two pointers: reverse

nums3=[43,42,41,40]

L=0
R=len(nums3)-1

while L<R:

    nums3[L] , nums3[R] = nums3[R] , nums3[L]
    L +=1
    R -=1

print(nums3)


#checking pallindrome
def pall(text):
    L=0
    R=len(text)-1

    while L < R:
        if text[L] != text[R]:
            return False
        L +=1
        R -=1
    return True


pall_text=input("Enter a text to check the pallindrome : ").strip().lower()

n=pall(pall_text)
print(n)