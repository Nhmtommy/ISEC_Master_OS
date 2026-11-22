def main():
    first_number = int(input("Enter the first number "))
    second_number = int(input("Enter the second number "))
    sum_of_numbers = first_number + second_number
    difference = first_number - second_number   
    product = first_number * second_number
    # what if second number is 0?
    if second_number <= 0:
        return print("Division by values <= zero is not allowed. Please enter a positive number second number.")
    else:
        quotient = first_number / second_number
        print(f"FOR {first_number} and {second_number}, Sum {sum_of_numbers}, Difference {difference}, Product {product}, Quotient {quotient}")

if __name__ == "__main__":
    main()
