print("Hi!")
while True:

    print("Safe Number Checker (Exception Handling)")
    print("__________")

    while True:
        try:
            user_input = input("Please enter a number: ")
            num = float(user_input)
            
            print(f"Thank you! You entered a valid number: {num} ✅")
            break
            
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz! (Please enter a valid number!) ⚠️")

    print("_________")
    again = input("Do you want to test again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break