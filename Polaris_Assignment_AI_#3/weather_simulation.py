import random

class Weather:
    def __init__(self):
        # The first day's weather is set to Sunny
        self.current_state = "Sunny"

    def predict_tomorrow(self):
        """Predicts tomorrow's weather based on today's using a Markov Model."""
        if self.current_state == "Sunny":
            # If today is Sunny: 80% Sunny, 20% Rainy
            self.current_state = random.choices(["Sunny", "Rainy"], weights=[80, 20], k=1)[0]
        elif self.current_state == "Rainy":
            # If today is Rainy: 30% Sunny, 70% Rainy
            self.current_state = random.choices(["Sunny", "Rainy"], weights=[30, 70], k=1)[0]
        
        return self.current_state

print("Hi!")
while True:
    print("AI Search: Uncertainty & Markov Models ☁️ ☀️")
    print("__________")
    print("Mission: 10-Day Weather Prediction Simulation.")
    
    try:
        # Create an instance of the Weather class
        simulator = Weather()
        
        # Day 1 is already known from __init__
        print(f"Day 1: {simulator.current_state} ☀️")
        
        # Loop to predict the next 9 days (totaling 10 days)
        for day in range(2, 11):
            next_day_weather = simulator.predict_tomorrow()
            icon = "☀️" if next_day_weather == "Sunny" else "🌧️"
            print(f"Day {day}: {next_day_weather} {icon}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e} ⚠️")

    print("_________")
    again = input("Do you want to run the simulation again? (yes/no): ").strip().lower()
    
    if again not in ["yes", "y"]:
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break
