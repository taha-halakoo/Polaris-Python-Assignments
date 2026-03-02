import random

def analyze_data(*args, **kwargs):
    """
    Advanced Data Analyzer using *args and **kwargs.
    Accepts any number of lists to analyze and specific keyword rules.
    """
    print("\n[System] Running Advanced Data Analysis... 🧙‍♂️✨")
    
    total_items = sum(len(data_list) for data_list in args)
    print(f"📊 Total records processed across {len(args)} dataset(s): {total_items}")
    
    print("🔍 Applied Filtering Rules:")
    if "min_age" in kwargs:
        print(f"   -> Minimum Age limit: {kwargs['min_age']}")
    if "starts_with" in kwargs:
        print(f"   -> Name Must Start With: '{kwargs['starts_with']}'")
    
    print("[System] Analysis complete. ✅\n")

print("Hi!")
while True:

    print("Data Wizard Simulation 🧙‍♂️")
    print("__________")
    
    # Generate some mock data
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Jack", "Aria", "Arthur", "Alex"]
    people = [{"name": random.choice(names), "age": random.randint(15, 60)} for _ in range(50)]
    
    print(f"Successfully generated a dataset of {len(people)} people! 📊")

    while True:
        print("__________")
        print("1. Show Raw Data (First 5 records) 📄")
        print("2. Filter: Age > 20 (List Comprehension) 🎂")
        print("3. Filter: Name starts with 'A' (List Comprehension) 🅰️")
        print("4. Run Advanced Analysis (*args / **kwargs) 🚀")
        print("5. End simulation for this dataset 🛑")
        
        choice = input("Select an action: ").strip()

        if choice == "5":
            print("Mission aborted... 🛑")
            break
        
        try:
            if choice == "1":
                print("\n📄 Raw Data Preview:")
                for p in people[:5]:
                    print(f" - {p}")
                print(" ...")
            elif choice == "2":
                # List comprehension for age > 20
                adults = [p for p in people if p["age"] > 20]
                print(f"\n🎂 Found {len(adults)} people older than 20:")
                for p in adults[:5]:
                    print(f" - {p}")
                if len(adults) > 5: print(" ...")
            elif choice == "3":
                # List comprehension for names starting with 'A'
                a_names = [p for p in people if p["name"].startswith('A')]
                print(f"\n🅰️ Found {len(a_names)} people whose name starts with 'A':")
                for p in a_names[:5]:
                    print(f" - {p}")
                if len(a_names) > 5: print(" ...")
            elif choice == "4":
                # Advanced function with *args and **kwargs
                analyze_data(people, min_age=20, starts_with='A', mode="Deep Scan")
            else:
                print("Unknown command. Try again! ⚠️")
        except Exception as e:
            print(f"An unexpected error occurred: {e} ⚠️")

    print("_________")
    again = input("Do you want to generate a new dataset? (yes/no): ").lower()
    
    if again not in ["yes", "y"]:
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break
