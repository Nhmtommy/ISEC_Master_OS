import math

def calculate_circle_area(radius):
    radius = int(radius)
    area = math.pi * (radius * radius)
    return area

def calculate_rectangle_area(length, width):
    length = int(length)
    width = int(width)
    area = length * width
    return area

def celsius_to_fahrenheit(celcius):
    celcius = int(celcius)
    fahrenheit = ((celcius * 9/5 ) + 32)
    return fahrenheit