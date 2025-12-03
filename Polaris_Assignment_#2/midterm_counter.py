from datetime import datetime

 #(with a little help of gemini about the library!😅)

print("Hi!")
while True:

    print("Exam Countdown Timer ⏳")
    print("Format: YYYY-MM-DD HH:MM (Year-Month-Day Hour:Minute)")
    print("__________")

    try:
        date_str = input("Enter exam date: ")
        
        exam_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        now = datetime.now()
        
        difference = exam_date - now
        
        days = difference.days
        hours = difference.seconds // 3600
        
        if difference.total_seconds() > 0:
            print(f"Time remaining: {days} days and {hours} hours! 📚")
            print("Keep studying!")
        else:
            print(f"This exam was {abs(days)} days ago. Hope you passed! 🎓")

    except ValueError:
        print("Invalid format! Please use YYYY-MM-DD HH:MM (e.g., 20XX-01-01 09:00)")

    print("_________")
    again = input("Do you want to calculate again? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break