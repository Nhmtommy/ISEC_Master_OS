import math_utility

def get_positive_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value < 0:
                print("Error Number cannot be negative. Try again")
                continue
            return value
        except ValueError:
            print("Error: Please Enter A Valid Number. Try Again")
    
def main():  
    celsius = ""
    radius = get_positive_number("Enter radius of circle :")
    length = get_positive_number("Enter Length of Rectangle :")
    width = get_positive_number("Enter width of Rectangle :")

    while True:
            try:
                 celsius= float(input("Enter degrees celsius :"))
                 break
            except ValueError:
                 print('Error: Please enter a valid number')


    circle_area = math_utility.calculate_circle_area(radius)
    rectangle_area = math_utility.calculate_rectangle_area(length,width)
    fahrenheit = math_utility.celsius_to_fahrenheit(celsius)
    print(f"CIRCLE AREA :{circle_area} RECTANGULAR AREA :{rectangle_area} FAHRENHEIT :{fahrenheit} ")


if __name__ == "__main__":
    main()