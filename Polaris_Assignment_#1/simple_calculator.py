print("Hi!")
while True:

    print("Simple Calculator")
    print("__________")

    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))

        print(f"Sum: {x + y:.2f}")
        print(f"Difference: {x - y:.2f}")
        print(f"Product: {x * y:.2f}")

        if y != 0:
            print(f"Quotient: {x / y:.2f}")
        else:
            print("Quotient: Undefined (Cannot divide by zero!)")
    except ValueError:
        print("Please enter valid numbers only.")

    print("_________")
    again = input("Do you want to calculate again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break