import math_utiliy

    
def main():  
    radius = ""
    length = ""
    width = ""
    celsius = ""
    while radius == "":
        radius = input("Enter Radius Of Circle :")
    while length == "":
        length = input("Enter length Of Rectangle :")
    while width == "":
        width = input("Enter Width Of Rectangle :")
    while celsius == "":
        celsius = input('Enter Degres is Celsius :')
        
    circle_radius = math_utiliy.calculate_circle_area(radius)
    rectangle_area = math_utiliy.calculate_rectangle_area(length,width)
    fahrenheit = math_utiliy.celsius_to_fahrenheit(celsius)
    
    print(f"CIRCLE AREA :{circle_radius} RECTANGULAR AREA :{rectangle_area} FAHRENHEIT :{fahrenheit}")
    
if __name__ == "__main__":
    main()