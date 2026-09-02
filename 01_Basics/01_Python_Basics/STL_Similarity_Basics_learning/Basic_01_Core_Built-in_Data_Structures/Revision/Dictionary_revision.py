#Basics
student ={
    "name" : "Nishant",
    "age" : 23
}

print(student["name"])

student["age"]=23.1
print(student["age"])
student["city"]="Pune"
print(student.get("ae","Not Found"))
print(student)
student.pop("city")
print("city" in student)
#Frequency counting

freq={}

text="banana"

for ch in text:
    # if ch in freq :
    #     freq[ch] += 1
    # else:
    #     freq[ch]=1
    freq[ch]=freq.get(ch,0)+1


for key, value in freq.items():
    print(f"{key} -> {value}")

freq2={}
nums=[1,2,3,4,5,2,1,2,5,6]
for x in nums:
    # if ch in freq :
    #     freq[ch] += 1
    # else:
    #     freq[ch]=1
    freq2[x]=freq2.get(x,0)+1

for key, value in freq2.items():
    print(f"{key} -> {value}")

























































