# DAILY REPORT — DAY 1

## 1. BIG BOOK EVIDENCE

- [x] Feynman Explanation: What is Software Engineering?

- [x] Trace of day1.py

- [x] Edge cases recorded 1. Enter nothing for name. Press Enter immediately
      Program runs succesfully,with no errors, however it skipped the name and just wrote "Hello, ! You are routhly 21 years old" 2. Enter abc for birth year.
      Programm crashd with Value error ; Invalid literal for int() . it didnt run. 3. Enter 2003.5 for birth year.
      Program ran successfully, however the age outputted is a negative value. which is practically impossible.
- [x] Engineering Thinking answers

1. Why does input() return a string instead of guessing the type?
   My response in book as it is Exactly: input() returns a string instead of guessing the type because string is a default type for the input() function and it helps to keep the program from crashing due to datatypes and keep it to change type at any time
2. Why use main() and the if **name** == "**main**": guard instead of just writing code at the top of the file?
   My response in book as it is Exactly: Beacuse **name** == "**main**": enables the py file to work as a module and as we can excecuted directly when working as amodule only, the function can be called in another program and if excecuted directly the function can be cslled drectly too. it helps to make sure tht function is not immedietly called when its working as module in another function.
3. We hardcoded current_year = 2026. What are the trade-offs of hardcoding vs. using datetime.date.today().year?
   My response in book as it is Exactly: since the years are variables, changing every year, using the datetime.date.today().year is helpful to keep the function, always up to date depending on present unlike writing it which might require updates every year and valunarable to errors.

- [x] Design Reflection answers

## 2. HANDS-ON CODE

- `day1.py` created, ran successfully, and committed.

def main():
print("=== Day 1: Welcome ===")
name = input("What is your name ?")
birth_year = int(input("What year were you born ? "))
current_year = 2026
age = current_year - birth_year
print(f"Hello, {name}! You are routhly {age} years old.")

if **name** == "**_main_**" :
main()

## 3. FIX THIS ANALYSIS

- **Bug 1:** [TypeError: unsupported operand type(s) for -: 'int' and 'str']. Root cause: [# date of birth was registred as string]. Fix: [# int() is added as parent of the input function to change age into integer in order to compute age].
- **Bug 2:** ["SyntaxError: '(' was never closed"]. Root cause: [# closing bracket was missing in the print statement]. Fix: [# closing bracket added].
- i could only find 2 bugs . now the program is running perfectly.

def main():
print("=== Day 1: Welcome ===")
name = input("What's your name? ")

    # I have added an int() to change birth_year so thatt the math works to compute the age.
    birth_year = int(input("What year were you born? "))
    current_year = 2026
    age = current_year - birth_year

    # closing bracket was missing in the print statement.
    print(f"Hello, {name}! You are roughly {age} years old.")

if **name** == "**main**":
main()

## 4. BUILD TASK SOLUTION

- `calculator.py` created.
- Handles division-by-zero edge case using an `if` statement.

## 6. SOLOLEARN EVIDENCE

- Question Link: [Insert Link]
- Answer: [Paste Answer]

## 7. DECLARATION

I declare all work is my own. I have not copy-pasted. I have not used AI without citation.

SIGNED: Kisuze Nahum, Day 1
