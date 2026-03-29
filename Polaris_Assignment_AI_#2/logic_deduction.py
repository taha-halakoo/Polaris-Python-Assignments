class Detective:
    """
    A Logic-based Inference Engine for the 'Clue' game.
    This class tracks suspects and eliminates possibilities as new evidence arrives.
    """
    def __init__(self):
        # The initial knowledge state: All are suspects.
        self.suspects = ["Colonel Mustard", "Professor Plum", "Miss Scarlett"]
        self.eliminated = []

    def eliminate_suspect(self, name):
        """Removes a suspect from the list of possibilities based on evidence."""
        # Normalize input to match list formatting
        normalized_name = name.strip().title()
        
        if normalized_name in self.suspects:
            self.suspects.remove(normalized_name)
            self.eliminated.append(normalized_name)
            print(f"✅ Evidence Received: {normalized_name} has been eliminated from the case.")
            return True
        else:
            print(f"⚠️  Logic Error: '{normalized_name}' is not in the current suspect pool.")
            return False

    def who_is_the_culprit(self):
        """Analyzes the current knowledge base to find the culprit."""
        count = len(self.suspects)
        
        if count == 1:
            print(f"🚨 DEFINITE INFORMATION: Culprit found! -> {self.suspects[0]} ⚖️")
        elif count > 1:
            print(f"🔍 STATUS: Not enough evidence yet. Potential suspects: {self.suspects} 🕵️‍♂️")
        else:
            print("🛑 LOGIC ERROR: Everyone has been eliminated! The investigation has collapsed. ❌")

# --- THE INTERACTIVE SIMULATION ---

print("Hi!")
while True:

    print("AI Knowledge Base: The Detective Simulation 🕵️‍♂️ 🧠")
    print("Mission: Use logical elimination to find the culprit.")
    print("__________")
    
    # Initialize the knowledge engine
    my_detective = Detective()

    while True:
        print("__________")
        print(f"Current Suspects: {my_detective.suspects} 🔍")
        print(f"Eliminated: {my_detective.eliminated} 📁")
        print("1. Add Evidence (Eliminate a Suspect) ➕")
        print("2. Check Culprit Status ⚖️")
        print("3. Reset Investigation 🔄")
        print("4. Close Case (Exit) 💤")
        
        choice = input("Select an action: ").strip()

        if choice == "4":
            print("Investigation terminated... 💤")
            break
        
        try:
            if choice == "1":
                print("\nPossible names: Colonel Mustard, Professor Plum, Miss Scarlett")
                target = input("Enter name to eliminate: ")
                my_detective.eliminate_suspect(target)

            elif choice == "2":
                print("\n--- INFERENCE REPORT ---")
                my_detective.who_is_the_culprit()

            elif choice == "3":
                my_detective = Detective()
                print("Knowledge base cleared! Investigation reset. 🔄")

            else:
                print("Unknown command. Try again! ⚠️")
        except Exception as e:
            print(f"An unexpected error occurred: {e} ⚠️")

    print("_________")
    again = input("Do you want to start a new investigation? (yes/no): ").lower()
    
    if again not in ["yes", "y"]:
        print("Good hunting! Case closed. Goodbye! 👋")
        input("Press Enter to close...")
        break
