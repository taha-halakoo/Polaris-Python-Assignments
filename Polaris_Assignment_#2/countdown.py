import time

print("Hi!")
while True:

    print("Rocket Countdown System 🚀")
    print("__________")

    try:
        start_num = int(input("Enter a number to start countdown: "))
        
        print(f"Starting countdown from {start_num}...")
        print("__________")
        

        for i in range(start_num, 0, -1):
            print(i)
            time.sleep(1) #I've used this to make it feel more realistic, as it decrements the numbers exactly every second!
        
        print("ATEŞLE! (FIRE!) 🚀🔥")

    except ValueError:
        print("Oops! Please enter a whole number (integer).")

    print("_________")
    again = input("Do you want to launch again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break