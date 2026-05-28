import random

def start_game():
    print("====================================")
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("I am thinking of a number between 1 and 100.")
    print("====================================")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            elif guess > secret_number:
                print("📉 Too high! Try a lower number.")
            else:
                print(f"\n🎉 Congratulations! You found the number in {attempts} attempts!")
                break 
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid whole number.")

def main():
    while True:
        start_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
