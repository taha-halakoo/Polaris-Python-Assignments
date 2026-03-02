class Rocket:
    def __init__(self, name, fuel_level):
        self.name = name
        self.fuel_level = int(fuel_level)

    def add_fuel(self, amount):
        self.fuel_level += amount
        print(f"Fuel added. New level: {self.fuel_level} ⛽")

    def launch(self):
        if self.fuel_level >= 10:
            print("Rocket launched successfully! 🌍 -> 🌕 🚀")
            self.fuel_level -= 10
        else:
            print("Error: Insufficient fuel! Please add fuel. ⚠️")

print("Hi!")
while True:

    print("Rocket Simulation 🚀")
    print("__________")

    rocket_name = input("Enter your rocket's name: ")

    while True:
        try:
            initial_fuel = int(input("Enter initial fuel level: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number. ⚠️")

    my_rocket = Rocket(rocket_name, initial_fuel)

    while True:
        print("__________")
        print(f"Current Rocket: {my_rocket.name} | Fuel: {my_rocket.fuel_level} ⛽")
        print("1. Launch Rocket 🚀")
        print("2. Refuel ⛽")
        print("3. End simulation for this rocket 🛑")
        
        choice = input("Select an action: ").strip()

        if choice == "3":
            print("Mission aborted... 🛑")
            break
        
        try:
            if choice == "1":
                my_rocket.launch()
            elif choice == "2":
                amount = int(input("Enter fuel amount to add: "))
                my_rocket.add_fuel(amount)
            else:
                print("Unknown command. Try again! ⚠️")
        except ValueError:
            print("Invalid input! Please enter a valid number. ⚠️")

    print("_________")
    again = input("Do you want to create a new rocket? (yes/no): ").lower()
    
    if again not in ["yes", "y"]:
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break
