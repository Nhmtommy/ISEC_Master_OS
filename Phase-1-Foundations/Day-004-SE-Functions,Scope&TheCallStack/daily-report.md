# DAILY REPORT — DAY 4: FUNCTIONS, SCOPE & THE CALL STACK

## 1. BIG BOOK EVIDENCE

- [x] Feynman Explanation: What is a function and why do we use them? (using a real-world analogy).
- [x] Trace: Call stack execution of `main()` calling `greet()`, which calls `print()`.
- [x] Edge cases recorded.
- [x] Engineering Thinking answers (3 questions).
- [x] Design Reflection answers (3 questions).
- [x] SoloLearn Feynman Practice (1 Q&A answer).

## 2. HANDS-ON CODE

- `day4.py` created, saved, ran successfully, and committed.
- `day4_broken.py` created, debugged, saved, ran successfully, and committed.

**Paste the final, working `day4.py` code here:**

```python
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
```

3. FIX THIS ANALYSIS

Bug 1:

· Description: [No output]
· Root cause: [Missing return statement]
· Fix: [adding returnn statement to return desired value]

Bug 2:

· Description: [variable scope error. NameError: name 'greeting_text' is not defined]
· Root cause: [print(greeting_text) was not indented to be under greet function however, the the greeting_text was a variable in greet function]
· Fix: [indentation of print(greeting_text) to be inside the greet function scope]

Bug 3:

· Description: [TypeError: add_numbers() missing 1 required positional argument: 'b']
· Root cause: [ one of the arguments for the function add_numbers() was missing]
· Fix: [argument "b" is added, as an integer or float]

4. BUILD TASK SOLUTION

· math_utils.py created with 3 separate functions.
· main.py created to import and test them.
· Handles the negative radius edge case with an early return.

Paste the complete math_utils.py code here:

```python
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
```

Paste the complete main.py code here:

```python
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
```

5. EDGE CASE REPORT

(Record the results of deliberately breaking day4.py)

· Test 1: Call calculate_area("five", 10).
· Observed behavior: [the area is fivefivefivefivefivefivefivefivefivefive]
· Analysis: [This is not acceptable because the required output is the area culculaated by multiplying 5 * 10]

· Test 2: Call calculate_area(5) (missing an argument).
· Observed behavior: [TypeError "missing a required positional argument "width" "]
· Analysis: [This is not acceptable, it throws an error to the user and crashes program]

· Test 3: Call a function before it is defined in the file.
· Observed behavior: [NameError "calculate area is not defined"]
· Analysis: [This is not acceptable, it throws an error to the user and crashes program]

6. SOLOLEARN EVIDENCE

```python
"""
this is how i did it on sololearn. helped him to improve.

https://sololearn.com/compiler-playground/c2DTgZwBhwjr/?ref=app
"""
color_r = input("Enter your current traffic light colour : ").upper()
print(color_r)
def colour():
    if color_r=="RED":
        print("\nPlease stop!!🤚🟥")
    elif color_r=="YELLOW":
        print("\nPlease ready for go! 🟡")
    elif color_r=="GREEN":
        print("\nYou can go..!!🟢")
    else:
        print("\nInvaild light colour!! Please enter the vaild traffic light colour")
colour()

"""
Grt Job.

This might be helpful for Reusable, testable and  Clean Code.
https://sololearn.com/compiler-playground/cda3qQmiMW19/?ref=app

"""
# request user name.
def user_name():
    get_name = input('Enter Your Name').upper()
    # loop if name == '' make sure user enters name before continuing.
    while get_name == '':
        get_name = input('Enter Your Name').upper()
    #function saved as user_name entered.
    return get_name

#request for Current Traffic Light Color.
def get_color():
    colors = ["RED","YELLOW","GREEN"]
    color_selected = ''
    # Loop to make sure color is a valid traffic light color.
    while color_selected not in colors:
            color_selected = input('Enter Your Current Traffic Light Color').upper()
    #function saved as color entered.
    return color_selected

#name and color passed to message as parameters
def show_message(name, color):
    if color == "RED":
        print(f"\n{name}\nPlease stop!! 🤚🟥")
    elif color == "YELLOW":
        print(f"\n{name}\nPlease get ready to go! 🟡")
    elif color == "GREEN":
        print(f"\n{name}\nYou can go..!! 🟢")


def main():
    name = user_name()
    color = get_color()
    show_message(name, color)

if __name__ == "__main__":
    main()
    """
7. DECLARATION

I declare all work is my own. I have not copy-pasted. I have not used AI without citation.
SIGNED: Kisuze Nahum, Day 4

```

## Github-repo : https://github.com/Nhmtommy/ISEC_Master_OS

```

```
