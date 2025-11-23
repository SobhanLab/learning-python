import random
import os

HIGHSCORE_FILE = "highscore.txt"


def clear_screen():
    """Console টা একটু পরিষ্কার করার জন্য (Windows / Mac / Linux সবায় কাজ করবে)।"""
    os.system("cls" if os.name == "nt" else "clear")


def load_highscore():
    """Highscore file থেকে পড়বে। না থাকলে None return করবে।"""
    if not os.path.exists(HIGHSCORE_FILE):
        return None

    try:
        with open(HIGHSCORE_FILE, "r") as f:
            data = f.read().strip()
            if not data:
                return None
            # format: difficulty,attempts
            difficulty, attempts = data.split(",")
            return {"difficulty": difficulty, "attempts": int(attempts)}
    except Exception:
        return None


def save_highscore(difficulty, attempts):
    """নতুন highscore ফাইলে লিখবে।"""
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(f"{difficulty},{attempts}")


def show_highscore():
    highscore = load_highscore()
    if highscore is None:
        print("📝 এখনো কোনো high score নেই.")
    else:
        print("🏆 Current High Score:")
        print(f"   Difficulty: {highscore['difficulty']}")
        print(f"   Attempts  : {highscore['attempts']}")


def choose_difficulty():
    """User থেকে difficulty নেবে এবং range + max_attempt দেবে।"""
    while True:
        print("\nChoose difficulty:")
        print("1) Easy   (1–50,   10 attempts)")
        print("2) Medium (1–100,   7 attempts)")
        print("3) Hard   (1–200,   5 attempts)")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            return "Easy", 1, 50, 10
        elif choice == "2":
            return "Medium", 1, 100, 7
        elif choice == "3":
            return "Hard", 1, 200, 5
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


def play_game():
    clear_screen()
    print("🎮 Number Guessing Game")
    difficulty_name, low, high, max_attempts = choose_difficulty()

    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ").strip()

        if not guess_input.isdigit():
            print("⚠ Please enter a valid positive number.")
            continue

        guess = int(guess_input)

        if guess < low or guess > high:
            print(f"⚠ Please enter a number within the range {low}–{high}.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! 📉\n")
        elif guess > secret_number:
            print("Too high! 📈\n")
        else:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"✅ You guessed it in {attempts} attempts.")

            # Highscore check
            highscore = load_highscore()
            if highscore is None or attempts < highscore["attempts"]:
                print("🏆 New high score! Saving it...")
                save_highscore(difficulty_name, attempts)
            else:
                print("ℹ You didn't beat the current high score this time.")

            break
    else:
        # Out of attempts
        print("\n😔 Out of attempts!")
        print(f"The correct number was {secret_number}.")

    input("\nPress Enter to return to main menu...")


def show_rules():
    clear_screen()
    print("📘 Game Rules")
    print("- Computer 1টা secret number নেয় নির্দিষ্ট range-এর মধ্যে।")
    print("- তুমি প্রতি বার একটা guess করবে.")
    print('- যদি guess ছোট হয়, বলবে "Too low!"')
    print('- যদি guess বড় হয়, বলবে "Too high!"')
    print("- Attempt limit শেষ হওয়ার আগে সঠিক ধরতে পারলে তুমি জিতে যাবে.")
    print("- কম attempt-এ ধরতে পারলে নতুন high score হওয়ার chance বেশি 😎")
    input("\nPress Enter to return to main menu...")


def main_menu():
    while True:
        clear_screen()
        print("===================================")
        print("   🎮 Number Guessing Game (CLI)   ")
        print("===================================")
        print("1) Play game")
        print("2) View rules")
        print("3) View high score")
        print("4) Exit")
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "3":
            clear_screen()
            show_highscore()
            input("\nPress Enter to return to main menu...")
        elif choice == "4":
            print("\nThanks for playing! Bye 👋")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3 or 4.")
            input("Press Enter to try again...")


if __name__ == "__main__":
    main_menu()
