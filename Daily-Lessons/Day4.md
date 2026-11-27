# Day 4 — Functions, Scope & the Call Stack

**Course:** Software Engineering Foundations  
**Day:** 4 of 365

---

## Section 1: Why This Matters Today

Yesterday, you wrote loops. If you write a 1,000-line script without functions, it is a nightmare to read, debug, and maintain. Today, you learn to build machines inside your code. Functions allow you to write a piece of logic once, give it a name, and use it anywhere. This is the foundation of all software architecture. Without functions, there is no software engineering.

---

## Section 2: The Idea (Feynman-Style)

Imagine you own a factory. You need to make a specific car part. You could hire a worker and tell them every single step from scratch every time you need the part. Or, you could build a machine that does it automatically. You put raw metal in, press a button, and the finished part comes out.

That machine is a function.

A function takes inputs (arguments), performs a task, and produces an output (return value).

```python
def calculate_area(length, width):
    area = length * width
    return area

# We "call" the machine
result = calculate_area(5, 10)
print(result)  # Output: 50
```

- `def` tells Python you are defining a function.
- `calculate_area` is the name of the machine.
- `length` and `width` are the inputs.
- `return` spits the output back out.

**Scope** means that variables created inside a function (like `area`) only exist inside that function. They are hidden from the rest of the program. This is a good thing. It prevents your code from getting tangled.

---

## Section 3: Under the Hood

When your program runs, the computer has a specific area of memory called the **Call Stack**.  
Think of it like a stack of plates in a cafeteria.

1. When your program starts, the `main()` function is placed on the stack (pushed).
2. When `main()` calls `calculate_area()`, the computer pauses `main()`, creates a new "frame" for `calculate_area()`, and puts it on top of the stack (pushed).
3. The computer executes `calculate_area()`. It calculates the area, returns the value, and then pops that frame off the stack. The memory used by `calculate_area` is instantly destroyed.
4. `main()` resumes exactly where it left off.

If a function calls itself, it pushes another frame onto the stack. If it does this too many times without stopping, the stack overflows, and the program crashes (StackOverflow).

---

## Section 4: Hands-On

Create `day4.py`. Type this and run it:

```python
def greet(name):
    message = f"Hello, {name}!"
    return message

def calculate_area(length, width):
    area = length * width
    return area

def main():
    # 1. Calling functions and storing outputs
    greeting = greet("Alice")
    print(greeting)

    # 2. Passing arguments
    room_area = calculate_area(5, 10)
    print(f"The area is {room_area}")

    # 3. Scope demonstration
    # print(message)  # Uncommenting this will cause a NameError! 'message' only exists inside greet().

if __name__ == "__main__":
    main()
```

Explanation:

- We define two functions: `greet` and `calculate_area`.
- We call them inside `main()`.
- The variables `message` and `area` are local to their functions. They are destroyed when the function ends.

---

## Section 5: Fix This

Save this as `day4_broken.py`. It contains 3 bugs. Run it, read the errors, and fix them.

```python
def add_numbers(a, b):
    result = a + b
    # Bug 1: Missing return statement

def greet(name):
    # Bug 2: variable scope error
    greeting_text = "Hello " + name

print(greeting_text)

def main():
    sum_result = add_numbers(5, 5)
    print(sum_result)  # Will print 'None' because of Bug 1

    greet("Alice")

    # Bug 3: Wrong number of arguments
    add_numbers(10)

if __name__ == "__main__":
    main()
```

---

## Section 6: Engineering Thinking

Answer these in your notebook:

1. Why is it better to return a value from a function (using `return`) rather than printing it inside the function?
2. What happens to the variables defined inside a function after the function finishes running?
3. If you have a function called `process_data()`, and you want to reuse it in another program, what do you need to do?

---

## Section 7: Professional Standards

1. **Single Responsibility Principle:** A function should do exactly ONE thing. If your function is called `get_user_data_and_send_email_and_update_database`, it is doing too much. Break it down.
2. **Naming:** Function names should be verbs. `calculate_area`, `get_user`, `save_file`. Variables should be nouns.
3. **The `return` statement:** A function should return a value. It should not just print it. `print` is for the user interface; `return` is for the program logic.

---

## Section 8: Edge Cases

Deliberately break `day4.py` and record the results in your notebook:

1. What happens if you call `calculate_area("five", 10)`?
2. What happens if you call `calculate_area(5)` (missing an argument)?
3. What happens if you call a function before it is defined in the file?

---

## Section 9: Design Reflection

Answer one sentence each in your notebook:

1. Could another programmer understand what your function does just by looking at its name and arguments?
2. If I needed to change the greeting message from "Hello" to "Hi", how many lines of code would I have to change?
3. Is a function easier to test than a raw block of code? Why?

---

## Section 10: Industry Connection

- **Web APIs:** Every endpoint you hit on a website (like `/api/users`) is backed by a function.
- **React Components:** In modern UI, every button, form, and page is a function.
- **Database:** When you call `db.save(user)`, you are calling a function written by the database engineers.
- **Math Libraries:** `math.sqrt(25)` is a function you will use constantly.

---

## Section 11: Your Turn & Notebook

### Build Task

Write `math_utils.py`. It must contain:

1. A function `calculate_circle_area(radius)`.
2. A function `calculate_rectangle_area(length, width)`.
3. A function `celsius_to_fahrenheit(celsius)`.

Then, write `main.py`. It must:

1. Import the functions from `math_utils.py`.
2. Ask the user for inputs.
3. Call the functions and print the results.
4. Handle the edge case where the user enters invalid input (e.g., negative radius) by printing an error message and returning early.

### Notebook (Write by Hand)

- **Feynman Explanation:** Explain what a function is and why we use them, using a real-world analogy (like a vending machine or a coffee grinder).
- **Trace:** Draw the call stack for this sequence: `main()` calls `greet()`, which calls `print()`.
- **Edge Cases:** List the results of Section 8.
- **Answers:** Engineering Thinking + Design Reflection.
- **SoloLearn:** Answer one Q&A question.

---

## Daily Report

Your Daily Report is due before midnight on 26 November.  
Submit the completed report, the code, and the link to your GitHub repository.

Signed,  
**Instructor**