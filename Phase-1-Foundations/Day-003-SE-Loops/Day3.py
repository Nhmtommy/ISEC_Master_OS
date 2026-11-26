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