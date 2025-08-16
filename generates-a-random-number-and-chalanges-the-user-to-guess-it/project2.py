import random

# Game difficulty parameters
DIFFICULTY_PARAMETERS = {
    '1': {'range': 50, 'attempts': 10},
    '2': {'range': 100, 'attempts': 7},
    '3': {'range': 1000, 'attempts': 5}
}

def get_valid_integer(prompt):
    """
    Prompts the user for a valid integer and handles ValueError exceptions.
    Keeps prompting until a valid integer is entered.
    """
    while True:
        try:
            user_input = input(prompt)
            # Handle empty input case
            if not user_input:
                print("Input cannot be empty. Please enter a number.")
                continue
            return int(user_input)
        except ValueError:
            print("That was no valid number. Please enter an integer.")

def get_difficulty():
    """
    Prompts the user to select a difficulty level and returns the game parameters.
    """
    print("\n--- Select Difficulty ---")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-1000, 5 attempts)")
    
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in DIFFICULTY_PARAMETERS:
            return DIFFICULTY_PARAMETERS[choice]
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def play_game():
    """
    Main game loop for a single round of the guessing game.
    """
    # 1. Get difficulty parameters from the user
    settings = get_difficulty()
    max_range = settings['range']
    max_attempts = settings['attempts']
    
    # 2. Generate the secret number
    secret_number = random.randint(1, max_range)
    print(f"\nI'm thinking of a number between 1 and {max_range}.")
    
    attempts_left = max_attempts
    
    # 3. The guessing loop
    while attempts_left > 0:
        print(f"\nYou have {attempts_left} attempts left.")
        prompt = f"Enter your guess (1-{max_range}): "
        try:
            guess = get_valid_integer(prompt)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting game...")
            return

        # 4. Check the guess
        if guess < 1 or guess > max_range:
            print(f"Your guess is out of the specified range (1-{max_range}). Try again.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {max_attempts - attempts_left + 1} attempts.")
            return True # Player won

        attempts_left -= 1
    
    # This part is reached if the while loop completes naturally (attempts_left = 0)
    print(f"\nGame over! You ran out of attempts. The number was {secret_number}.")
    return False # Player lost

def main():
    """
    Main entry point for the program. Controls the "play again" loop.
    """
    print("--- Welcome to the Number Guessing Game! ---")
    
    # The outer loop for playing multiple rounds
    while True:
        # Run a single game session
        play_game()
        
        while True:
            play_again = input("\nPlay again? (Y/N): ").strip().lower()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print("\nThanks for playing! Goodbye.")
                return # Exit the main function, terminating the program
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main()