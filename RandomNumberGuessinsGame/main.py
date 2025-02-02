import random

while True:
    lowest_number = 1
    highest_number = 100
    guess_attempts = 0
    answer = random.randint(lowest_number, highest_number)
    print(f"Guess a number between {lowest_number} and {highest_number}: ")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        guess_attempts += 1
        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        else:
            print(f"Correct! You guessed it in {guess_attempts} attempts")
            break

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
