# Mini project : Student Management System (Inheritance)

# class Student: 
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

# class Students(Student):
#     def __init__(self, name, age, course):
#         super().__init__(name, age, course)
#         self.course = course

#     def show_student(self):
#         print(f"{self.name} studies {self.course}")

#     def show_info(self):
#         print(f"Name : {self.name}")
#         print(f"Age : {self.age}")
#         print(f"Course: {self.course}")

# student1 = Student("Ali", 20, "Python")

# print(student1.name)
# print(student1.age)
# print(student1.course)
        
# student1.show_info()

# student = [
#     student1,
#     student2,
#     student3
# ]

## jawapan selepas dibetulkan :

class Student: 
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Course : {self.course}")


# simpan semua student (DATABASE simple)
students = []

# create objects
student1 = Student("Ali", 20, "Python")
student2 = Student("Siti", 22, "Data Science")
student3 = Student("Ahmad", 21, "AI")

# masukkan ke list
students.append(student1)
students.append(student2)
students.append(student3)

# loop semua student
for student in students:
    student.show_info()
    print("-----")

## Bahagian 3: Add, view, Exit.

while True:
    print(f"Studen Management System")
    print("1.Add student")
    print("2. View ")
    print("3. Exit")

    choice = input("Choose option : ")

    if choice == "1":
        name = input ("Enter name")
        age = int(input("Enter age"))
        course = input("Enter Course")
    
        student = Student(name, age, course)
        students.append(student)

        print("Student added succesfully")
    
    if choice == "2":
        if len(students) == 0:
            print("No students found")

        else:
            for student in students:  # nested for
                student.show_info()
                print("----")
    
    if choice == "3":
        print("GoodBye!")
        break

    else:
        print("Invalid Option")