print("Hi!")
while True:

    print("Give me your score and I'll tell you whether you passed or failed!")
    print("_________")

    while True:
        try:
            grade = float(input("Enter your exam grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    if grade > 50:
        print("Result: Passed ✅")
    else:
        print("Result: Failed ❌")

        print("_________")
    again = input("Do you want to calculate again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break