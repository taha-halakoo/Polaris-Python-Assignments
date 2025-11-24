print("Hi!")
while True:
    print("\n--- 100 Years Calculator ---")
    name = input("What is your name? ")
    
    try:
        age = int(input("How old are you? "))
        
        current_year = 2025
        years_left = 100 - age
        year_turning_100 = current_year + years_left

        print(f"Hello {name}, you will turn 100 in the year {year_turning_100}.")
    except ValueError:
        print("Please enter a valid number for age.")

    print("_________")
    again = input("Do you want to calculate again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break