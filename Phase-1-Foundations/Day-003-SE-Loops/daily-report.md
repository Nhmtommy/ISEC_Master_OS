# DAILY REPORT — DAY 3: LOOPS (WHILE, FOR & ITERATION PATTERNS)

## 1. BIG BOOK EVIDENCE

- [x] Feynman Explanation: `for` loops vs `while` loops (using a real-world analogy).
- [x] Trace: Execution of `guess_game.py` with the secret `7` and guesses `3`, `9`, `7`.
- [x] Edge cases recorded.
- [x] Engineering Thinking answers (3 questions).
- [x] Design Reflection answers (3 questions).
      for question 2.

```python
def main():
    #1. basic for loop
    print("---Countdown---")
    for i in range (5, 0, -1): #Start at 5, stop before 0, step -1
        print(i)
    print("Liftoff")

    #2. Loop over a list
    print("\n--- Names ---")
    names = [ "Alice", "Bob", "Charlie" ]
    for name in names:
        print(f"Hello, {name} " )

    #3. WHile loop with input validation
    print("\n---Security Check ---")
    correct_pin = "1234"
    entered_pin = ""
    counter = 0
    #keep looping as long as the pin is wrong
    while entered_pin != correct_pin:
        entered_pin = input("Enter Your PIN :")
        if entered_pin !=correct_pin and counter <= 3:
            print("Incorrect. Try again. ")
            counter += 1
        else:
            print("Access denied")
    print("Access Granted")
4 lines Changed to limit attempts.

if __name__ == "__main__":
    main()




- [x] SoloLearn Feynman Practice (1 Q&A answer).
      IN BIG BOOK ATTACHED Day3.pdf
```

## 2. HANDS-ON CODE

- `day3.py` created, saved, ran successfully, and committed.
- `day3_broken.py` created, debugged, saved, ran successfully, and committed.

**Paste the final, working `day3.py` code here:**

```python
def main():
    #1. basic for loop
    print("---Countdown---")
    for i in range (5, 0, -1): #Start at 5, stop before 0, step -1
        print(i)
    print("Liftoff")

    #2. Loop over a list
    print("\n--- Names ---")
    names = [ "Alice", "Bob", "Charlie" ]
    for name in names:
        print(f"Hello, {name} " )

    #3. WHile loop with input validation
    print("\n---Security Check ---")
    correct_pin = "1234"
    entered_pin = ""

    #keep looping as long as the pin is wrong
    while entered_pin != correct_pin:
        entered_pin = input("Enter Your PIN :")
        if entered_pin !=correct_pin:
            print("Incorrect. Try again. ")
    print("Access Granted")

if __name__ == "__main__":
    main()
```

## 3. FIX THIS ANALYSIS

````python
def main():
    #Bug 1: Infinite loop
    count = 1
    while count <= 5:
        count += 1
        print(f"Counting, {count}" )
    #loop was meant to count from 1 to 5. bug raesulted into infinite loop. however bug is fixed with rational logic for counting to 5

    #Bug 2:Off-By-One error
    print("Even numbers")
    for i in range(1,5):
            if i % 2 != 1:
                print(i)
    # initually printed values were not even numbers. between 1 and 5 . logic fixed to oget desired output

    #Bug 3: Syntax/Logic error
    for i in range(3): #Missing colon at the end . status "Fixed"
        print("Loop iteration", i)


if __name__ == "__main__":
    main()
    ```
**Bug 1:**

- Description: [Infinite loop]
- Root cause: [While True in program resulted into an infine loop without break]
- Fix: [loop was meant to count from 1 to 5. bug raesulted into infinite loop. however bug is fixed with rational logic for counting to 5.{Code Provided}]

**Bug 2:**

- Description: [ initually printed values were not even numbers. between 1 and 5 .]
- Root cause: [it was due to wrong logic for outputting even numbers]
- Fix: [logic fixed to oget desired output used % to check foro even ]

**Bug 3:**

- Description: [Syntax/Logic error]
- Root cause: [#for i in range(3): #Missing colon at the end ]
- Fix: [added colon at the end of statement]


## 4. BUILD TASK SOLUTION

- `guess_game.py` created.
- Meets all requirements: handles too high/low, uses a `while` loop, limits to 5 guesses, and breaks on a correct guess.

**Paste the complete `guess_game.py` code here:**

```python
def main():
    #Hard coded number
    secret = 7
    count = 0
    guess = int(input("Guess The Number :"))
    while guess != secret and count < 5 :
        count += 1
        if(guess > secret):
            print(f"Too High {count}")
            guess = int(input("Guess The Number :"))
        elif(guess < secret):
            print("Too Low")
            guess = int(input("Guess The Number :"))
    if guess == secret:
        print("You Win")
    else:
        print("Game Over")

if __name__ == "__main__":
    main()
````

## 5. EDGE CASE REPORT

_(Record the results of deliberately breaking `day3.py`)_

- **Test 1:** Enter `1234` the first time in the PIN loop.
  - Observed behavior: [Program outputted Access Granted]
  - Analysis: [This is acceptable because the entered password is exactly the required ]
- **Test 2:** Create a `for` loop with a range of `range(0)`.
  - Observed behavior: [when ran nothing is outputted.]
  - Analysis: [this might be acceptable of its intended to loop 0 times . however it can be a bug if not intended ]
- **Test 3:** Type `abc` in the PIN loop.
  - Observed behavior: [Program outputted Incorrect. Try again. ]
  - Analysis: [This is acceptable because a password can be numerical, alphabetical lor evne mixed with soecial characters as well.]

## 6. SOLOLEARN EVIDENCE

- Question Link: [https://www.sololearn.com/Discuss/3374244/?ref=app]
  " ppl, I've learned html and css completely but whenever I try to code my head gets empty, i have no idea what to code, i get overwhelmed with so many tags I've learned but i don't know where to use them"
- Answer: [Blank head is not because u don't know HTML. it's because u think about all tags at once, for a simple practice u only need a few tags. And don't try to force perfection, it results to analysis paralysis making you forget or loss your decision ability. You now know what to build, just get started although it might seem ugly. <h1> <div> <p> <input> <button> are enough for start.
  ]

## 7. DECLARATION

I declare all work is my own. I have not copy-pasted. I have not used AI without citation.
SIGNED: Kisuze Nahum, Day 3
