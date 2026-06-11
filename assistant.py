import random


software_data = [
                 'System Software: Controls the core operations of your device, including hardware management, memory, and security. Examples include operating systems like Microsoft Windows, macOS, Linux, Android, and iOS.',
                 'Designed to help users perform specific tasks, such as creating documents, browsing the internet, or playing games. Examples include web browsers like Google Chrome, productivity suites like Microsoft 365, and mobile applications.',
                 'Programming Software: Tools used by developers and programmers to write, test, debug, and maintain other software and programs. Examples include code editors, compilers, and Integrated Development Environments (IDEs) like Visual Studio.'
                 ]

def detect_intent(user_input):

    text = user_input.lower()

    if any(w in text for w in ["software","website","application","ios","android"]):
        return "software"

def generate_text(intent):

    if intent == "software":
        return random.choice(software_data)
    
    else:
        return "Data Not Available for the given Domain"

while True:
    user_input = input("You :")

    if user_input == "exit":
        print("Good Bye ! ")
        break

    intent = detect_intent(user_input)
    result = generate_text(intent)
    print(f"Response -> {result}")