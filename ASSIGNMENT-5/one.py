n=int(input("Enter the no of students"))
students={}
for i in range (n):
    name=input("Enter the name of student:  ")
    marks=input("Enter the marks of student: ")
    students[name]=marks

print(students)

name=input("Enter the student's name :: ")

if name in students:
    print(f"{name}'s marks: {students[name]} ")
else:
    print("Students not found.")
    