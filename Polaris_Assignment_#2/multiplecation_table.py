print("Hi!")
while True:

    print("Master Multiplication Table (1-9)")
    print("__________")

    input("Press Enter to generate the table...")
    print()

    for i in range(1, 10):

        for j in range(1, 10):
            result = i * j

            print(f"{i}x{j}={result:<2}", end="  ")
        
        print()
    
    print("__________")
    again = input("Do you want to see it again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break