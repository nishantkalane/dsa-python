
student={
    "name":"nishant",
    "age":23
}


student["city"]="Pune" #add
print(student)
student["age"]="24 Running" # change
print(student)
student.pop("age") #remove
print(student)
print(student.get("age", "Not Found"))#safely get value
print(student)
print("name" in student) #check if key exist
print("age" in student)
print(len(student)) #number of key value pairs

