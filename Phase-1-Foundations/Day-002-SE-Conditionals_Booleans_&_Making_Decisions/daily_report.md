# DAILY REPORT — DAY 2: CONDITIONALS, BOOLEANS & MAKING DECISIONS

## 1. BIG BOOK EVIDENCE

- [x] Feynman Explanation:

imagine biology teacher coming into class and says,only those with marks atleast 80% will be awarded by the biology department, those between 50 to 79 wont get anything while those below 50 will be punished, this is exactly how conditions work, we can sort each category of the biology class individuals using conditions . if elif and else.

- [x] Trace: Execution of `day2.py` with inputs (Age=20, Score=85, Temp=-5).
      In big book (big book scans day 2)

- [x] Edge cases recorded.
      DONE in this document

- [x] Engineering Thinking answers (3 questions).

1. Why use if/elif/else instead of three separate if statements for the grade logic? What happens if score is 95 with three separate ifs?

2. We convert input() to int() immediately. What happens if the user types "ninety" instead of "90"?

3. Could the grade logic be extracted into its own function get_grade(score)? Why might that be better?

- [x] Design Reflection answers (3 questions).

1. Could another programmer understand this code in 30 seconds?

2. If I needed to add a new grade category (e.g., "A+"), how many lines must change?

3. Is the logic testable? Could I write a function that takes a score and returns a grade, then test it separately?

- [x] SoloLearn Feynman Practice (1 Q&A answer).

## 2. HANDS-ON CODE

- `day2.py` created, saved, ran successfully, and committed.
- `day2_broken.py` created, debugged, saved, ran successfully, and committed.

**Paste the final, working `day2.py` code here:**

```python
def main():
    #Simple if else
    age = int(input("Enter your age "))
    if age >= 18:
        print("You can vote")
    else:
        print("You are too young to vote")
    # else if chain
    score = int(input("Enter your score (0-100):"))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Your grade is {grade}")

    #combining conditionals with 'and'
    temp = int(input("Enter temperature in Celsius"))
    if temp > 0 and temp < 100:
        print("Water is liquid")
    else:
        print("Water is not liquid")

if __name__ == "__main__":
    main()

```

## 3. FIX THIS ANALYSIS

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

if **name** == "**main**":
main()

**Bug 1:**

- Description: [SyntaxError: expected ':']
- Root cause: [: at the end of a conditional sytatement was missing .]
- Fix: [Adding the : at the end of conditional statement
  with errors. if password == "secret".
  fixed. if password == "secret":
  ]

**Bug 2:**

- Description: [SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?]
- Root cause: [use of = which is for assignment in a conparision == should be used instead]
- Fix: [i replace = with == to work as comaprision ]
  with error. if number = 0:
  fixed. if number == 0:

**Bug 3:**

i found only 2 bugs and fixed them. now program is running without any errors.

## 4. BUILD TASK SOLUTION

- `login.py` created.
- Meets all requirements: checks `"admin"` and `"1234"`, handles incorrect username, incorrect password, and successful login.

**Paste the complete `login.py` code here:**

```python
def main():

# default user name and password
    name = "admin"
    password = 1234
# user name and password

    user_name = input("Enter User Name ")
    user_password = int(input("Enter Password "))
#conditions for user approval to login only if anme and password are both correct
    if user_name == name  and user_password == password:
        print("Login successful")
    elif user_name != name:
        print("User not found")
    elif user_password != password:
        print("Incorrect password")

if __name__ == "__main__":
    main()
```

## 5. EDGE CASE REPORT

_(Record the results of deliberately breaking `day2.py`)_

- **Test 1:** Enter `-5` for age.
  - Observed behavior: [outputted your too young to vote]
  - Analysis: [this is not acceptable because no negative age exists. thefore its a bug can be solved by retuning till user inputs age >= 0]
    def main():
    age = int(input("Enter your age "))
    if age < 0:
    main()
    elif age >= 18:
    print("You can vote")
    else:
    print("You are too young to vote")
    main()

- **Test 2:** Enter `105` for score.
  - Observed behavior: [it outputs "Your grade is A]
  - Analysis: [this is not acceptable because score range is exceeded]
    this can be solved by aloop tht ensures tht the range is strictly between 0 - 100.

- **Test 3:** Enter `abc` for temperature.
  - Observed behavior: [
    it threw a ValueError: invalid literal for int() with base 10: 'abc'
    ]
  - Analysis: [this is not acceptable because it an crash the entire program . ]
    this can be solved by putting constraints to only allow input as a Number.

## 6. SOLOLEARN EVIDENCE

- Question Link: [Insert Link]
- Answer: [Paste your Feynman-style answer here]

## 7. DECLARATION

I declare all work is my own. I have not copy-pasted. I have not used AI without citation.
SIGNED: Kisuze Nahum, Day 2
