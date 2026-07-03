numbers= []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    num = int(input("Enter number {i + 1}: ")) # i disini bermaksud, angka giliran nombor, bukan kiraan
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print(f"Results:")
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")