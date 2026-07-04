subject = {"Math", "Science", "English"}
Grades = {"A", "B", "C", "D", "F"}
Student = {"Alice", "Bob", "Charlie"}

subject.add("History")  # Adding a new subject
subject.remove("English")  # Removing a subject
subject.discard("Geography")  # Discarding a subject that may not exist (no error if it doesn't)

print(subject.union(Grades))  # Output: {'Math', 'Science', 'English', 'A', 'B', 'C', 'D', 'F'}
print(Student.intersection(Grades))  # Output: set() since there are no common elements

#guna add, remove, discard, and pop methods untuk manipulate sets