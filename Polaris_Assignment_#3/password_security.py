import re

while True:
    password = input("\nCreate a password: ")

    issues = []

    if not re.search(r"[A-Z]", password):
        issues.append("missing uppercase letter")

    if not re.search(r"\d", password):
        issues.append("missing number")

    if not re.search(r"[^A-Za-z0-9]", password):
        issues.append("missing special character")

    if not issues:
        print("Password accepted. Security level: STRONG 🔒")
    else:
        print("Password rejected. Issues found:")
        for issue in issues:
            print("-", issue)

    choice = input("\nDo you want to try another password? (y/n): ").lower()
    if choice != "y":
        print("Password security check finished.")
        break
