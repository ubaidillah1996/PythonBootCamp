number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


# for loop : count
# while loop : condition
# (start, end, step(scale))
# for ada 2, continue dan break
# nested guna i : parent, j : children
# cara nested berfungsi : loop parent akan loop dulu, baru loop children.
# loop parent akan jalan sekali, skip, pergi ke children sampai habis, continue loop parent.
