def main():
    print("=== Day 1: Welcome ===")
    name = input("What's your name? ")

    # I have added an int() to change birth_year so thatt the math works to compute the age.
    birth_year = int(input("What year were you born? "))
    current_year = 2026
    age = current_year - birth_year
    # closing bracket was missing in the print statement.
    print(f"Hello, {name}! You are roughly {age} years old.")

if __name__ == "__main__":
    main()
