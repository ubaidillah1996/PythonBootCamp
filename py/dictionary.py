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

# print(students_records)

# Exercise 2 : add new student .

new_student = {
    "Name" : "Mike",
    "ID" : "student_003",
    "Age" : 18,
    "Major" : "Math",
    "Grades" : [82,79,91]
}

students_records.append(new_student)

print(students_records)

# Exercise 3 : Update Jon's age to 20

# for student in students_records: 
#     if student["Name"] == "John":
#         student["Age"] = 20

# print(students_records)


# # Exercise 4 : Loop all # display semua maklumat

# for student in students_records:
    # print(student["ID"],student["Name"],student["Major"])
