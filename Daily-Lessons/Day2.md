# Day 2 — Conditionals, Booleans & Making Decisions

**Course:** Software Engineering Foundations  
**Day:** 2 of 365  
**Status:** Day 2

---

## Section 1: Why This Matters Today

A program that cannot make decisions is not software — it is a script that blindly repeats the same actions. A login page must reject wrong passwords. A banking system must check if a balance is sufficient. Today, you give your programs the power to branch — to examine data and choose a path.

---

## Section 2: The Idea (Feynman-Style)

Imagine a bouncer at a club.  
The rule is: IF you are over 18, THEN you can enter. ELSE, you are turned away.

That is a conditional. The condition (`age > 18`) evaluates to either `True` or `False`. These are Booleans, named after George Boole.

In Python, you write it like this:

```python
if age >= 18:
    print("Enter")
else:
    print("Go home")
```

If the first condition is False, you can check another: `elif` (else if).

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

The computer checks these from top to bottom. As soon as it finds a `True` condition, it executes that block and skips the rest.

---

## Section 3: Under the Hood

When the Python compiler processes an `if` statement, it converts it into bytecode using jump instructions.

1. It evaluates the condition (e.g., `age >= 18`).
2. If the result is `False`, it executes a `POP_JUMP_IF_FALSE` instruction. This literally tells the instruction pointer in the CPU to skip over the indented block of code and jump to the `else` block.
3. If `True`, it just executes the next line sequentially.

At the hardware level, the CPU uses logic gates to compare the values and set a flag, which the jump instruction checks.

---

## Section 4: Hands-On

Create `day2.py`. Type this and run it:

```python
def main():
    # Simple if/else
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You can vote.")
    else:
        print("You are too young to vote.")

    # elif chain
    score = int(input("Enter your score (0-100): "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Your grade is {grade}.")

    # Combining conditions with 'and'
    temp = int(input("Enter temperature in Celsius: "))
    if temp > 0 and temp < 100:
        print("Water is liquid.")
    else:
        print("Water is not liquid.")

if __name__ == "__main__":
    main()
```

Explanation:

- `>=` means greater than or equal to.
- `and` requires **BOTH** sides to be `True`.
- `elif` is only checked if the previous `if` was `False`.

---

## Section 5: Fix This

Save this as `day2_broken.py`. It contains 3 bugs. Run it, read the errors, and fix them.

```python
def main():
    password = input("Enter password: ")
    if password == "secret"
        print("Access granted.")
    else:
        print("Access denied.")

    number = int(input("Enter a number: "))
    if number = 0:
        print("Zero")
    elif number > 0:
        print("Positive")
    else:
        print("Negative")

if __name__ == "__main__":
    main()
```

---

## Section 6: Engineering Thinking

Answer these in your Big Book:

1. Why use `if`/`elif`/`else` instead of three separate `if` statements for the grade logic? What happens if `score` is 95 with three separate `if`s?
2. We convert `input()` to `int()` immediately. What happens if the user types `"ninety"` instead of `"90"`?
3. Could the grade logic be extracted into its own function `get_grade(score)`? Why might that be better?

---

## Section 7: Professional Standards

1. **No `=` for comparison:** Always use `==` when checking if two values are equal in a condition.
2. **Indentation:** Exactly 4 spaces for the code block inside an `if` statement.
3. **No redundant conditions:** If you use `else`, you don't need to check `elif condition == False`. The `else` handles the rest.

---

## Section 8: Edge Cases

Deliberately break `day2.py` and record the results in your Big Book:

1. Enter `-5` for age.
2. Enter `105` for score. Does the program handle it, or does it give an A?
3. Enter `abc` for temperature. What error do you get?

---

## Section 9: Design Reflection

Answer one sentence each in your Big Book:

1. Could another programmer understand this code in 30 seconds?
2. If I needed to add a new grade category (e.g., "A+"), how many lines must change?
3. Is the logic testable? Could I write a function that takes a score and returns a grade, then test it separately?

---

## Section 10: Industry Connection

- **Authentication:** `if hash(input_password) == stored_hash: login()`
- **Game engines:** `if player.health <= 0: respawn()`
- **E-commerce:** `if cart.total > 100: free_shipping = True`
- **Operating systems:** `if process.state == "ready": schedule()`

---

## Section 11: Your Turn & Big Book

### Build Task

Write `login.py`. It must:

1. Have a hardcoded username `"admin"` and password `"1234"`.
2. Ask the user for username and password.
3. If both match, print `"Login successful."`
4. If username is wrong, print `"User not found."`
5. If username is correct but password is wrong, print `"Incorrect password."`
6. Use only `if`/`elif`/`else` and `and`. No loops.

### Big Book (Write by Hand)

- **Feynman Explanation:** Explain `if`/`elif`/`else` and Boolean logic using a real-world analogy (traffic lights, a bouncer, etc.).
- **Trace:** Trace the execution of `day2.py` with the inputs: Age=20, Score=85, Temp=-5.
- **Edge Cases:** List the results of Section 8.
- **Answers:** Engineering Thinking + Design Reflection.
- **SoloLearn:** Answer one Q&A question.

---

## Daily Report

Your Daily Report is due before midnight.  
Submit it with the link to your GitHub repository.

Signed,  
**Instructor**