# DAILY REPORT — DAY 1

## 1. BIG BOOK EVIDENCE

- [x] Feynman Explanation: What is Software Engineering?
- [x] Trace of day1.py
- [x] Edge cases recorded
- [x] Engineering Thinking answers
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

## 5. EDGE CASE REPORT

- Input: `abc` for birth year. Result: `ValueError` crash.
- Input: `2003.5` for birth year. Result: `ValueError` crash.
- Input: `2027` for birth year. Result: Negative age. Not handled.

## 6. SOLOLEARN EVIDENCE

- Question Link: [Insert Link]
- Answer: [Paste Answer]

## 7. DECLARATION

I declare all work is my own. I have not copy-pasted. I have not used AI without citation.

SIGNED: Kisuze Nahum, Day 1
