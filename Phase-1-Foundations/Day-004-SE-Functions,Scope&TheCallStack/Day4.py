def greet(name):
    message = f"Hello, {name}"
    return message

def calculate_area(length, width):
    area = length * width
    return area

def main():
    # 1. Calling functions and storing outputs
    greeting = greet("Nahum")
    print(greeting)

    # 2. Passing arguments
    room_area = calculate_area(5,10)
    print(f"The area is {room_area}")

    # 3. Scope demostration
    # print(message) #Uncommenting this will cause a NameError! 'mesaage' only exists inside greet() 

if __name__ == "__main__":
    main()

"""
EXPLANATION
1. We define two functions greet and calculate_area.
2. We call them inside main()
3. The variables message and area are local to their functions. 
   They are destroyed when the function ends 
"""