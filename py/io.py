<<<<<<< HEAD
name = input("Enter your name: ")
height = int(input("Enter your height in meters: "))

while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0 and age < 80:
            break
        else:
            print("Age must be a positive integer between 1 and 79. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")


print(f"Hello {name}!")
print(f"Your height is {height} meters.")
print(f"Your age is {age} years.") 

=======
name = input("Enter your name: ")
height = int(input("Enter your height in meters: "))

while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0 and age < 80:
            break
        else:
            print("Age must be a positive integer between 1 and 79. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")


print(f"Hello {name}!")
print(f"Your height is {height} meters.")
print(f"Your age is {age} years.") 

>>>>>>> a6f5ec4 (Initial commit)
