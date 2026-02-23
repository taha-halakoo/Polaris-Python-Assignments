class Roket:
    def __init__(self, isim, yakit_seviyesi):
        self.isim = isim
        self.yakit_seviyesi = int(yakit_seviyesi)

    def yakit_doldur(self, miktar):
        self.yakit_seviyesi += miktar
        print(f"Yakıt eklendi. Yeni seviye: {self.yakit_seviyesi}")

    def firlat(self):
        if self.yakit_seviyesi >= 10:
            print("Roket başarıyla fırlatıldı! 🌍 -> 🌕")
            self.yakit_seviyesi -= 10
        else:
            print("Hata: Yetersiz yakıt! Lütfen yakıt doldurun.")

print("Hi!")
while True:

    print("Rocket Simulation 🚀")
    print("__________")

    roket_name = input("Enter your rocket's name: ")

    while True:
        try:
            initial_fuel = int(input("Enter initial fuel level: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    my_rocket = Roket(roket_name, initial_fuel)

    while True:
        print("__________")
        print(f"Current Rocket: {my_rocket.isim} | Fuel: {my_rocket.yakit_seviyesi}")
        print("1. Launch Rocket")
        print("2. Refuel")
        print("3. End simulation for this rocket")
        
        choice = input("Select an action: ").strip()

        if choice == "3":
            print("Mission aborted...")
            break
        
        try:
            if choice == "1":
                my_rocket.firlat()
            elif choice == "2":
                amount = int(input("Enter fuel amount to add: "))
                my_rocket.yakit_doldur(amount)
            else:
                print("Unknown command. Try again! ⚠️")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("_________")
    again = input("Do you want to create a new rocket? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break