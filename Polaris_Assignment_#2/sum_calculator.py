print("Hi!")
while True:
    print("Sum Calculator (1 to N)")
    print("__________")

    try:
        n = int(input("Enter a number (N): "))

        if n < 1:
            print("Please enter a number greater than 0.")
        elif n > 10**18:
            # Warning for extremely large numbers
            print("⚠️ That number is extremely large! Calculation might be impractical.")
            print("⚠️ Bu sayı çok büyük! Hesaplanması pek pratik olmayabilir.")
        else:
            # Fast formula
            total_sum = n * (n + 1) // 2

            print(f"Calculated sum of numbers from 1 to {n}:")
            print(f"Result: {total_sum} ✨")

    except ValueError:
        print("Oops! That's not a valid number.")

    print("_________")
    again = input("Do you want to calculate again? (yes/no): ").lower()

    if again not in ("yes", "y"):
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break
