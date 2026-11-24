def main():
    #Simple if else
    age = int(input("Enter your age "))
    if age >= 18:
        print("You acn vote")
    else:
        print("You are too young to vote")
    # else if chain
    score = int(input("Enter your score (0-100):"))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Your grade is {grade}")

    #combining conditionals with and