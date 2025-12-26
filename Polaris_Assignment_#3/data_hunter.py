import re

email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
phone_regex = r"\+?\d[\d\s-]{8,}\d"

while True:
    print("\n--- DATA HUNTER ---")
    print("1) Use broken data file")
    print("2) Paste broken data manually")
    print("3) Exit")

    choice = input("Select an option: ").strip()

    if choice == "3":
        print("Exiting Data Hunter. Goodbye.")
        break

    if choice == "1":
        level = input("Choose data level (1 or 2): ").strip()

        if level == "1":
            input_file = "broken_data_level1.txt"
            output_file = "clean_directory_level1.txt"
        elif level == "2":
            input_file = "broken_data_level2.txt"
            output_file = "clean_directory_level2.txt"
        else:
            print("Invalid level.")
            continue

        try:
            with open(input_file, "r", encoding="utf-8") as file:
                text = file.read()
        except FileNotFoundError:
            print("Broken data file not found.")
            continue

    elif choice == "2":
        print("Paste your broken data below.")
        print("Type 'END' on a new line to finish:\n")

        lines = []
        while True:
            line = input()
            if line == "END":
                break
            lines.append(line)

        text = "\n".join(lines)
        output_file = "clean_directory_manual.txt"

    else:
        print("Invalid option.")
        continue

    emails = set(re.findall(email_regex, text))
    phones = set(re.findall(phone_regex, text))

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("EMAILS FOUND:\n")
        for email in emails:
            file.write(email + "\n")

        file.write("\nPHONE NUMBERS FOUND:\n")
        for phone in phones:
            file.write(phone + "\n")

    print("\nData hunting completed.")
    print(f"Emails found: {len(emails)}")
    print(f"Phone numbers found: {len(phones)}")
    print(f"Results saved to '{output_file}'.")

    again = input("\nDo you want to hunt more data? (y/n): ").lower()
    if again != "y":
        print("Session ended.")
        break
