# Day 3 — Loops: while, for & Iteration Patterns

**Course:** Software Engineering Foundations  
**Day:** 3 of 365  
**Status:** Day 3

---

## Section 1: Why This Matters Today

A program that cannot repeat an action is a calculator. A program that can repeat an action is a system. Today, you learn how to make your code do the heavy lifting. Loops are the engines of software. Whether you are processing a million database records, rendering frames in a video game, or waiting for a user to enter a valid password, you will use loops.

---

## Section 2: The Idea (Feynman-Style)

Imagine you have to write "I will not skip code" on a chalkboard 100 times. You could write 100 separate `print` statements. But that is inefficient and prone to errors.

Instead, you write a rule: "Start at 1. If the number is less than or equal to 100, write the sentence, add 1 to the number, and repeat."

That is a loop.

In Python, there are two main types of loops:

1. **`for` loops:** Used when you know exactly how many times you want to repeat (e.g., "do this 10 times", or "do this for every item in a list").
2. **`while` loops:** Used when you want to repeat until a condition changes (e.g., "keep asking for a password until it is correct").

```python
# A for loop: Do this 5 times
for i in range(5):
    print(f"Count: {i}")

# A while loop: Keep going until condition is False
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted.")
```

---

## Section 3: Under the Hood

How does the computer know how to loop? It does not have a physical loop. It uses jump instructions.  
When the Python compiler sees a loop, it translates it into bytecode that says:

1. Evaluate the condition.
2. If the condition is False, jump to the end of the loop block.
3. Execute the loop body.
4. Jump back to step 1 (the `JUMP_ABSOLUTE` instruction).

If the condition never becomes False (e.g., `while True:`), the computer will jump back forever. This is an **infinite loop**. It will consume all your CPU and freeze your terminal. You must always ensure your loop has an exit condition.

---

## Section 4: Hands-On

Create `day3.py`. Type this and run it:

```python
def main():
    # 1. Basic for loop
    print("--- Countdown ---")
    for i in range(5, 0, -1):  # Start at 5, stop before 0, step -1
        print(i)
    print("Liftoff!")

    # 2. Loop over a list
    print("\n--- Names ---")
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(f"Hello, {name}!")

    # 3. While loop with input validation
    print("\n--- Security Check ---")
    correct_pin = "1234"
    entered_pin = ""

    # Keep looping as long as the pin is wrong
    while entered_pin != correct_pin:
        entered_pin = input("Enter your PIN: ")
        if entered_pin != correct_pin:
            print("Incorrect. Try again.")

    print("Access granted.")

if __name__ == "__main__":
    main()
```

Explanation:

- `range(5, 0, -1)` generates numbers starting at 5, stopping before 0, stepping by -1.
- `while entered_pin != correct_pin:` will keep executing the indented block until the user types `"1234"`.

---

## Section 5: Fix This

Save this as `day3_broken.py`. It contains 3 bugs. Run it, read the errors, and fix them.

```python
def main():
    # Bug 1: Infinite loop
    count = 1
    while count <= 5:
        print("Counting:", count)

    # Bug 2: Off-by-one error
    print("Even numbers:")
    for i in range(1, 5):
        print(i)

    # Bug 3: Syntax/Logic error
    for i in range(3)
        print("Loop iteration", i)

if __name__ == "__main__":
    main()
```

---

## Section 6: Engineering Thinking

Answer these in your notebook:

1. When would you use a `while` loop instead of a `for` loop?
2. What happens if the condition in a `while` loop never becomes `False`?
3. Look at the `range(1, 5)` in the broken code. How many times does it run? What if you wanted it to include the number 5?

---

## Section 7: Professional Standards

1. **Infinite Loops:** Never write a loop without an explicit exit condition. If you use `while True:`, you must include a `break` statement.
2. **Meaningful Variables:** Do not use `i`, `j`, `k` unless it is a simple counter. If you are looping over names, call the variable `name`. If you are looping over users, call it `user`.
3. **Nested Loops:** If you nest a loop inside a loop, indent exactly 4 spaces for each level. Keep it readable.

---

## Section 8: Edge Cases

Deliberately break `day3.py` and record the results in your notebook:

1. What happens if you enter `1234` the first time in the PIN loop? Does it print `"Incorrect"`?
2. What happens if you create a `for` loop with a range of `range(0)`? Does it run at all?
3. What happens if you type `abc` in the PIN loop? (It won't crash because it's a string, but what does the logic do?)

---

## Section 9: Design Reflection

Answer one sentence each in your notebook:

1. Could another programmer understand this code in 30 seconds?
2. If I wanted to limit the PIN attempts to 3 tries, how many lines would change?
3. Is the loop logic testable? How would you write a test for a loop?

---

## Section 10: Industry Connection

- **Web servers:** `while True:` runs the main server loop, waiting for HTTP requests.
- **Data processing:** A `for` loop processes every row in a database.
- **Games:** A `while` loop runs the game engine, calculating the next frame 60 times a second.
- **Security:** A `while` loop limits login attempts to prevent brute-force attacks.

---

## Section 11: Your Turn & Notebook

### Build Task

Write `guess_game.py`. It must:

1. Have a hardcoded secret number (e.g., `secret = 7`).
2. Have a `while` loop that asks the user to guess the number.
3. If the guess is too high, print `"Too high."`
4. If the guess is too low, print `"Too low."`
5. If the guess is correct, print `"You win!"` and `break` out of the loop.
6. Limit the user to a maximum of 5 guesses. If they fail 5 times, print `"Game Over."` and exit.

### Notebook (Write by Hand)

- **Feynman Explanation:** Explain `for` loops vs `while` loops using a real-world analogy (e.g., counting steps vs waiting for a bus).
- **Trace:** Trace the execution of `guess_game.py` if the secret is 7 and the user guesses 3, 9, 7.
- **Edge Cases:** List the results of Section 8.
- **Answers:** Engineering Thinking + Design Reflection.
- **SoloLearn:** Answer one Q&A question.

---

## Daily Report

Your Daily Report is due before midnight on 25 November.  
Submit the completed report, the code, and the link to your GitHub repository.

Signed,  
**Instructor**