print("Hi!")
while True:

    print("Check if a number is positive, negative, or zero.")
    print("__________")

    try:
        num = float(input("Enter a number: "))

        if num > 0:
            print(f"The number {num} is Positive (+).")
        elif num < 0:
            print(f"The number {num} is Negative (-).")
        else:
            print("The number is exactly Zero (0).")
    except ValueError:
        print("Oops! That's not a valid number.")

    print("_________")
    again = input("Do you want to calculate again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break