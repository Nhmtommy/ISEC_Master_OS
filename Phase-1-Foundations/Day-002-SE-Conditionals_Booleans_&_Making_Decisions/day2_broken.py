def main():
    password = input("Enter password: ")
    if password == "secret":

        print("Access granted.")
    else:
        print("Access denied.")

    number = int(input("Enter a number: "))
    if number == 0:
        print("Zero")
    elif number > 0:
        print("Positive")
    else:
        print("Negative")

if __name__ == "__main__":
    main()
