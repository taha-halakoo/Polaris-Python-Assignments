class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        """Adds a node to the frontier (LIFO)"""
        self.frontier.append(node)

    def contains_state(self, state):
        """Checks if a state exists in the frontier"""
        return any(node == state for node in self.frontier)

    def empty(self):
        """Checks if the frontier is empty"""
        return len(self.frontier) == 0

    def remove(self):
        """Removes the last node added (LIFO)"""
        if self.empty():
            raise Exception("Empty frontier! ⚠️")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        """Removes the first node added (FIFO) - BFS logic"""
        if self.empty():
            raise Exception("Empty frontier! ⚠️")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# --- THE INTERACTIVE SIMULATION ---

print("Hi!")
while True:

    print("AI Search: The Frontier Simulation 🔍 🧠")
    print("__________")
    print("Mission: Visualize DFS (Stack) vs BFS (Queue) logic.")
    
    # Let's create both to compare!
    stack = StackFrontier()
    queue = QueueFrontier()

    while True:
        print("__________")
        print(f"Stack (DFS/LIFO) Items: {stack.frontier} 📚")
        print(f"Queue (BFS/FIFO) Items: {queue.frontier} 👥")
        print("1. Add Data (Push) ➕")
        print("2. Remove Data (Pop) ➖")
        print("3. Reset Frontiers 🔄")
        print("4. End AI Simulation 🛑")
        
        choice = input("Select an action: ").strip()

        if choice == "4":
            print("AI Simulation Offline... 🛑")
            break
        
        try:
            if choice == "1":
                data = input("Enter a value (Node) to add: ")
                stack.add(data)
                queue.add(data)
                print(f"Added '{data}' to both frontiers! ✅")

            elif choice == "2":
                if not stack.empty():
                    s_node = stack.remove()
                    q_node = queue.remove()
                    print(f"\n--- POP RESULTS ---")
                    print(f"DFS (Stack) removed: {s_node} (Last In, First Out) 📚")
                    print(f"BFS (Queue) removed: {q_node} (First In, First Out) 👥")
                else:
                    print("Error: Frontiers are empty! Add data first. ⚠️")

            elif choice == "3":
                stack = StackFrontier()
                queue = QueueFrontier()
                print("Frontiers reset successfully! 🔄")

            else:
                print("Unknown command. Try again! ⚠️")
        except Exception as e:
            print(f"An unexpected error occurred: {e} ⚠️")

    print("_________")
    again = input("Do you want to start a new search simulation? (yes/no): ").lower()
    
    if again not in ["yes", "y"]:
        print("See you later! Goodbye! 👋")
        input("Press Enter to close...")
        break
