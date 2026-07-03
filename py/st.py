subject = {"Math", "Science", "English"}
Grades = {"A", "B", "C", "D", "F"}
Student = {"Alice", "Bob", "Charlie"}

print(subject.union(Grades))  # Output: {'Math', 'Science', 'English', 'A', 'B', 'C', 'D', 'F'}
print(Student.intersection(Grades))  # Output: set() since there are no common elements
