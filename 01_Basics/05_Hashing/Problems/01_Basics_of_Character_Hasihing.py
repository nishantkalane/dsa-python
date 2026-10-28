
s = "aabedcfghhgdfagtlkjrshtoeuAFHGSUIJR2734890i"
check_times=int(input("How Many letters you want to check ? :"))

hash_array = [0]*256

for i in range(len(s)):
    hash_array[ord(s[i])] +=1

while check_times >0:
    c = input("Which Letter you want to cross check : ")
    print(hash_array[ord(c)])
    check_times -=1
 #O(m+n) m = initilaize list and n =build frequency list
 #SC = O(m)