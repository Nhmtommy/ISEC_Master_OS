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