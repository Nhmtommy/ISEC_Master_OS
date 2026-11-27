# Day 1 — What Software Engineering Really Is & Your First Program

**Course:** Software Engineering Foundations  
**Day:** 1 of 365  
**Status:** Course Initiated

---

## Section 1: Why This Matters Today

You are not here to learn Python syntax. You are here to learn how to build systems that do not collapse. Today, you will write your first program, but more importantly, you will understand the engineering mindset that separates a professional from a hobbyist. Every future lesson depends on this foundation.

---

## Section 2: The Idea (Feynman-Style)

Imagine you need to cross a stream. You throw a wooden plank across and walk over. That works — once. But if a hundred people must cross every day for twenty years, in rain and wind, you need a bridge. You need to think about load, materials, maintenance, and what happens when the water rises.

Writing code is throwing a plank across a stream. Software engineering is designing the bridge.

Software engineering means:

1. Understand the problem before touching the keyboard.
2. Design a solution others can reason about. Code is read ten times for every time it is written.
3. Verify it works correctly. Not just “it ran once without crashing.” Edge cases matter.
4. Manage change over time. Requirements shift.

That process is a loop:

**Understand → Specify → Design → Build → Verify → Validate → Deploy & Maintain**

Today, we touch step 4 (**Build**). But always see it inside the whole cycle.

---

## Section 3: Under the Hood

When you type `python3 day1.py` and press Enter in your WSL2 Ubuntu terminal:

1. The shell reads your command, finds the Python executable, and launches a process.
2. The Python interpreter initializes: allocates memory, loads built-in modules.
3. The interpreter reads `day1.py`. The lexer converts bytes into tokens: `print`, `(`, `"Hello"`, `)`.
4. The parser arranges tokens into an Abstract Syntax Tree (AST).
5. The compiler walks the AST and emits bytecode for the Python Virtual Machine (PVM).
6. The PVM executes the bytecode. `print` is looked up, pushed to the stack, and calls the OS `write()` syscall.
7. The OS writes the bytes to standard output. Your terminal renders them.

No magic. Just layers of translation.

---

## Section 4: Hands-On

Create a file named `day1.py` in your WSL2 environment. Type this exactly:

```python
# day1.py — First software engineering artifact

def main():
    print("=== Day 1: Welcome ===")
    name = input("What's your name? ")
    birth_year = int(input("What year were you born? "))
    current_year = 2026
    age = current_year - birth_year
    print(f"Hello, {name}! You are roughly {age} years old.")

if __name__ == "__main__":
    main()
```

Explanation:

- `def main():` defines a function; it does not run yet.
- `input()` pauses, waits for keyboard input, returns a string.
- `int()` converts the input string into an integer so math works.
- `f"Hello, {name}!"` is an f-string, embedding variables directly.
- `if __name__ == "__main__":` is the guard that runs `main()` only if this file is executed directly.

---

## Section 5: Fix This

Save this as `day1_broken.py`, run it, read the errors, and fix all three bugs.

```python
def main():
    print("=== Day 1: Welcome ===")
    name = input("What's your name? ")
    birth_year = input("What year were you born? ")
    current_year = 2026
    age = current_year - birth_year
    print(f"Hello, {name}! You are roughly {age} years old."

if __name__ == "__main__":
    main()
```

---

## Section 6: Engineering Thinking

Answer these in your Big Book:

1. Why does `input()` return a string instead of guessing the type?
2. Why use `main()` and the `if __name__ == "__main__":` guard instead of just writing code at the top of the file?
3. We hardcoded `current_year = 2026`. What are the trade-offs of hardcoding vs. using `datetime.date.today().year`?

---

## Section 7: Professional Standards

Non-negotiable:

1. **Naming:** `lowercase_with_underscores`. Meaningful names.
2. **Indentation:** Exactly 4 spaces. Never mix tabs and spaces.
3. **Comments:** Explain **WHY**, not **WHAT**.
4. **Structure:** Always use `main()` and the entry-point guard.

---

## Section 8: Edge Cases

Deliberately break `day1.py`. Record each result in your Big Book.

1. Enter nothing for name. Press Enter immediately.
2. Enter `abc` for birth year.
3. Enter `2003.5` for birth year.
4. Enter a number greater than 2026.

---

## Section 9: Design Reflection

Answer one sentence each in your Big Book:

1. Could another programmer understand this code in 30 seconds?
2. If I needed to ask for a middle name too, how many lines would change?
3. Is this code testable?

---

## Section 10: Industry Connection

- CLI tools like `git`, `docker`, `aws`: parse input, process, output.
- Web servers (Django/Flask): receive HTTP request (structured input), run code, return response.
- Logging systems: process billions of `print()` equivalents to log files.
- REPLs: the Python shell is just `while True: input() → eval() → print()`.

---

## Section 11: Your Turn & Big Book

### Build Task

Write `calculator.py`. It must:

1. Have a `main()` function.
2. Ask for two numbers (floats or ints).
3. Print the sum, difference, product, and quotient.
4. Handle the quotient edge case (what happens if the second number is `0`?).
5. Follow all Professional Standards.

### Big Book (Write by Hand)

- **Feynman Explanation:** “What is software engineering?” (Half page, no code, your own analogy).
- **Trace:** Draw a step-by-step flowchart of what happens when `python3 day1.py` runs.
- **Edge Cases:** List every way you broke the program in Section 8.
- **Answers:** Engineering Thinking + Design Reflection.
- **SoloLearn:** Answer one Q&A question (Feynman style) and copy it here.

---

## Daily Report

Your Daily Report is due.

It must include:

1. Big Book evidence (photos or text summary).
2. Hands-on code.
3. Fix This analysis (bug, root cause, fix).
4. Build Task code.
5. Edge case report.
6. SoloLearn evidence.
7. Signed declaration.

Get to work. When you are done, submit the report.

Signed,  
**Instructor**