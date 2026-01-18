import re
import os # We need this to check if files exist

# --- REGEX PATTERNS ---
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
phone_pattern = r"\+?\d[\d\s-]{8,}\d"

print("Welcome to Data Hunter! 🕵️‍♂️")

while True:
    print("__________")
    print("1. Scan Existing Level Files")
    print("2. Manual Input (via 'manual_input.txt')") # <--- CHANGED
    print("3. Exit")
    
    choice = input("Select your mission: ").strip()
    
    text_content = ""
    output_filename = ""
    
    if choice == "3":
        print("Mission aborted. Goodbye! 👋")
        break

    try:
        if choice == "1":
            level = input("Select Level (1 or 2): ").strip()
            if level == "1":
                input_filename = "lvl1_bozuk_veri.txt"
                output_filename = "lvl1_temiz_rehber.txt"
            elif level == "2":
                input_filename = "lvl2_bozuk_veri.txt"
                output_filename = "lvl2_temiz_rehber.txt"
            else:
                print("Invalid level! ❌")
                continue
                
            with open(input_filename, "r", encoding="utf-8") as file:
                text_content = file.read()
                print(f"Read successful from {input_filename} ✅")

        elif choice == "2":
            # --- THE NEW SMART WAY ---
            input_filename = "manual_input.txt"
            output_filename = "manual_temiz_rehber.txt"
            
            # 1. Create the file if it doesn't exist so the user can find it
            if not os.path.exists(input_filename):
                with open(input_filename, "w", encoding="utf-8") as f:
                    f.write("") # Create empty file
            
            print(f"\n⚠️  TERMINAL PASTE IS UNSTABLE.")
            print(f"👉  Please open '{input_filename}' on your computer.")
            print(f"👉  Paste your data there, SAVE the file, and close it.")
            
            # 2. Wait for the user to be ready
            input("⌨️   Press Enter here once you have saved the file... ")
            
            # 3. Read the file
            with open(input_filename, "r", encoding="utf-8") as file:
                text_content = file.read()
            
            if not text_content.strip():
                print("❌  The file is empty! Did you forget to save?")
                continue
                
            print("Data captured successfully! ✅")

        else:
            print("Unknown command. Try again! ⚠️")
            continue

        # --- MINING PROCESS ---
        emails = set(re.findall(email_pattern, text_content))
        phones = set(re.findall(phone_pattern, text_content))

        with open(output_filename, "w", encoding="utf-8") as file:
            file.write("--- FOUND EMAILS ---\n")
            for email in emails:
                file.write(f"{email}\n")
            
            file.write("\n--- FOUND PHONES ---\n")
            for phone in phones:
                file.write(f"{phone}\n")

        print(f"Success! Data saved to '{output_filename}' 💾")
        print(f"Stats: {len(emails)} emails and {len(phones)} phone numbers found. 📊")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. 📁❌")
    except Exception as e:
        print(f"An unexpected error occurred: {e} ⚠️")

    print("__________")
    again = input("Do you want to hunt more data? (yes/no): ").lower()
    if again not in ["yes", "y"]:
        print("Good hunting! 👋")
        input("Press Enter to close...")
        break