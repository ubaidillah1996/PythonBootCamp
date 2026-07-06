# Exercise 1 : create a dictionary called student_records with these informations.

students_records = [
    {
    "Name" : "John",
    "ID" : "student_001",
    "Age" : 19,
    "Major" : "Computer Science",
    "Grades" : [85, 92, 78]
    },
    {
    "Name" : "Sarah",
    "ID" : "student_002",
    "Age" : 20,
    "Major" : "Biology",
    "Grades" : [90,88,95]
    }
]

# Exercise 2 : add new student .

new_student = {
    "Name" : "Mike",
    "ID" : "student_003",
    "Age" : 18,
    "Major" : "Math",
    "Grades" : [82,79,91]
}

students_records.append(new_student)

# Exercise 3 : Loop all

for student in students_records:
    print(student["ID"],student["Name"],student["Major"])