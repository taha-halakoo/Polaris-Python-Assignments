import datetime

class Assistant:
    def __init__(self, name):
        self.name = name
        self.operation_count = 0

    def greet(self, user_name):
        self.operation_count += 1
        print(f"Hello {user_name}, I am {self.name}. How can I help you? 🤖")

    def status_report(self):
        print(f"I have performed {self.operation_count} operations so far. 📊")
        
    def check_time(self):
        self.operation_count += 1
        now = datetime.datetime.now().strftime("%H:%M")
        print(f"The time is {now}. Time flies! ⏰")

print("Hi!")
while True:

    print("AI Assistant Setup 🤖")
    print("__________")

    assistant_name = input("Give your AI assistant a name: ")
    user_name = input("What is your name? ")

    my_assistant = Assistant(assistant_name)

    while True:
        print("__________")
        print(f"Assistant: {my_assistant.name} | Status: Online 🟢")
        print("1. Greet me 👋")
        print("2. What time is it? ⏰")
        print("3. Status Report 📊")
        print("4. Turn Off 💤")
        
        choice = input("Select an action: ").strip()

        if choice == "4":
            print(f"{my_assistant.name} is going to sleep. 💤")
            break
        
        try:
            if choice == "1":
                my_assistant.greet(user_name)
            elif choice == "2":
                my_assistant.check_time()
            elif choice == "3":
                my_assistant.status_report()
            else:
                print("Unknown command. Try again! ⚠️")
        except Exception as e:
            print(f"An unexpected error occurred: {e} ⚠️")

    print("_________")
    again = input("Do you want to set up a new assistant? (yes/no): ").lower()
    
    if again not in ["yes", "y"]:
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break
