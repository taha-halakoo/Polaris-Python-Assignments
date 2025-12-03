import random

print("Hi!")
while True:

    print("Number Guessing Game (1-100) 🎲")
    print("I have picked a number. Can you guess it?")
    print("__________")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Wrong! Go Up! (Yukarı çık) ⬆️")
            elif guess > secret_number:
                print("Wrong! Go Down! (Aşağı in) ⬇️")
            else:
                print(f"CORRECT! The number was {secret_number}. 🎉")
                print(f"You found it in {attempts} attempts.")
                break
                
        except ValueError:
            print("Please enter a valid integer (whole number).")

    print("_________")
    again = input("Do you want to play again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break