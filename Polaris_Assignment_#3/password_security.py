import re

def check_password_strength(password):
    """
    Analyzes password and returns a list of missing requirements.
    If list is empty, password is strong.
    """
    issues = []

    # Check for Uppercase
    if not re.search(r"[A-Z]", password):
        issues.append("Missing uppercase letter (A-Z)")

    # Check for Number
    if not re.search(r"\d", password):
        issues.append("Missing number (0-9)")

    # Check for Special Character
    if not re.search(r"[^A-Za-z0-9]", password):
        issues.append("Missing special character (!@#...)")

    return issues

# This block ensures the loop ONLY runs when you play the game,
# not when the test file imports the function.
if __name__ == "__main__":
    print("Password Security System 🛡️")
    
    while True:
        print("__________")
        user_pass = input("Enter a password to test: ")
        
        result_issues = check_password_strength(user_pass)
        
        if len(result_issues) == 0:
            print("Status: STRONG ✅")
            print("Access Granted!")
        else:
            print("Status: WEAK ⚠️")
            print("Issues found:")
            for issue in result_issues:
                print(f" - {issue}")
        
        print("__________")
        again = input("Test another password? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("Stay safe! 👋")
            input("Press Enter to close...")
            break
