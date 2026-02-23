import datetime

class Asistan:
    def __init__(self, isim):
        self.isim = isim
        self.islem_sayisi = 0

    def selam_ver(self, kullanici_adi):
        self.islem_sayisi += 1
        print(f"Merhaba {kullanici_adi}, ben {self.isim}. Sana nasıl yardım edebilirim?")

    def durum_raporu(self):
        print(f"Bugüne kadar toplam {self.islem_sayisi} işlem gerçekleştirdim.")
        
    def saat_kac(self):
        self.islem_sayisi += 1
        now = datetime.datetime.now().strftime("%H:%M")
        print(f"Şu an saat {now}. Zaman çok hızlı geçiyor!")

print("Hi!")
while True:

    print("AI Assistant Setup 🤖")
    print("__________")

    assistant_name = input("Give your AI assistant a name: ")
    user_name = input("What is your name? ")

    my_assistant = Asistan(assistant_name)

    while True:
        print("__________")
        print(f"Assistant: {my_assistant.isim} | Online")
        print("1. Greet me")
        print("2. What time is it?")
        print("3. Status Report")
        print("4. Turn Off")
        
        choice = input("Select an action: ").strip()

        if choice == "4":
            print(f"{my_assistant.isim} is going to sleep. 💤")
            break
        
        try:
            if choice == "1":
                my_assistant.selam_ver(user_name)
            elif choice == "2":
                my_assistant.saat_kac()
            elif choice == "3":
                my_assistant.durum_raporu()
            else:
                print("Unknown command. Try again! ⚠️")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("_________")
    again = input("Do you want to set up a new assistant? (yes/no): ").lower()
    
    if again != "yes" and again != "y":
        print("Goodbye! 👋")
        input("Press Enter to close...")
        break