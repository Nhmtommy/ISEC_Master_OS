def main():
    #Bug 1: Infinite loop
    count = 1
    while count <= 5:
        count += 1
        print(f"Counting, {count}" )
    #loop was meant to count from 1 to 5. bug raesulted into infinite loop. however bug is fixed with rational logic

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