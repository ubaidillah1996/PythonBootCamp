
score = 0

answer1 = input("What is your favourite movie? ")
if answer1.capitalize() == "Angel Has Fallen":
    print("Correct!")
    score += 1

answer2 = input("What is the colour of your motorcycle? ")
if answer2.capitalize() == "Red":
    print("Correct!")
    score += 1

answer3 = input("What is your favourite game? ")
if answer3.capitalize() == "Dota 2":
    print("Correct!")
    score += 1

print(f"Your final score is: {score}")  


