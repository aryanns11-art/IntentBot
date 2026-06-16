import random
import json
import pyttsx3
import re
import speech_recognition as sr

try:
    with open("data-sets.json", "r") as file:
        data = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    print("Error loading dataset!")
    exit()

knowledge_base = data["knowledge_base"]
keywords = data["keywords"]

#---------------------------------------------------------------------------------------------  

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
#---------------------------------------------------------------------------------------------  

def contains_phrase(text, phrase):
    pattern = r"\b" + re.escape(phrase) + r"\b"
    return re.search(pattern, text) is not None

#---------------------------------------------------------------------------------------------  
 
def detect_intent(user_input):
    text = user_input.lower()

    for main_domain, data in keywords.items():

        if any(contains_phrase(text, phrase) for phrase in data["main"]):   

            for sub_domain, sub_words in data["sub"].items():

                if any(contains_phrase(text, phrase) for phrase in sub_words):
                    return (main_domain, sub_domain)

            print(f"\nBot: Main topic found: {main_domain}")
            print("Please choose a sub-topic:\n")

            sub_list = list(data["sub"].keys())

            for i, sub in enumerate(sub_list, start=1):
                print(f"{i}. {sub}")

            choice = input("\nEnter choice number: ")

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= len(sub_list):
                    selected = sub_list[choice - 1]
                    return (main_domain, selected)

            return (main_domain, "unknown")

    return ("unknown", "unknown")

#---------------------------------------------------------------------------------------------

def generate_text(intent, mode="explanation"):

    main_domain, sub_domain = intent

    greetings = [
        "Sure! ",
        "Here's something about that: ",
        "Let me explain: ",
        "Good question! "
    ]

    if main_domain not in knowledge_base:
        return "Data Not Available Yet!"
    
    if sub_domain not in knowledge_base[main_domain]:
        return f"I recognized the topic '{main_domain}', but I don't have information on '{sub_domain}' yet."

    topic_data = knowledge_base[main_domain][sub_domain]

    if mode not in topic_data:
        return "I don’t have that info yet."

    return random.choice(greetings) + random.choice(topic_data[mode])

#---------------------------------------------------------------------------------------------

def get_followup_response(intent, f_type):

    main_domain, sub_domain = intent

    try:
        if f_type == "examples":
            return random.choice(knowledge_base[main_domain][sub_domain]["examples"])

        elif f_type == "explanation":
            return random.choice(knowledge_base[main_domain][sub_domain]["explanation"])

        else:
            return "I don't have more on that yet."

    except:
        return "I don’t have that information yet."

#---------------------------------------------------------------------------------------------

def is_valid_intent(intent):
    main_domain, sub_domain = intent

    if main_domain not in knowledge_base:
        return False

    return sub_domain in knowledge_base[main_domain]

#---------------------------------------------------------------------------------------------

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
                
        try:
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)

            print(f"You (Voice): {text}")

            return text.lower()

        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return ""

        except sr.RequestError:
            print("Speech service unavailable.")
            return ""

#---------------------------------------------------------------------------------------------

def mainn():

    followups = [
        ("Want me to explain more? ", "explanation"),
        ("Do you want examples? ", "examples"),
        ("Should I go deeper into this? ", "explanation")
    ]
    
    last_intent = None
    mode = input("Type 'v' for voice or 't' for text: ").lower()

    while True:

        if mode == "v":
            user_input = listen()
        else:
            user_input = input("You: ")

        if not user_input:
            continue    

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            speak("Goodbye !")
            break

        intent = detect_intent(user_input)

        if intent == ("unknown", "unknown") and last_intent:
            intent = last_intent
        else:
            last_intent = intent

        response = generate_text(intent, mode="explanation")
        print(f"Bot: {response}")
        speak(response)

        if not is_valid_intent(intent):
            continue

        question, f_type = random.choice(followups)

        print("Bot: ",question)
        speak(question)

        if mode == "v":
            choice2 = listen()
        else:
            choice2 = input("You: ").lower()

        if not choice2:
            continue

        if any(word in choice2 for word in ["yes", "yeah", "sure", "ok", "okay"]):
            extra = get_followup_response(intent, f_type)
            print(f"Bot: {extra}")
            speak(extra)           

        elif any(word in choice2 for word in ["no", "nah", "nope"]):
            res = "Alright! Ask me something else"
            print(f"Bot: {res}")
            speak(res)

mainn()

#for main_domain, data in keywords.items():
#--Understanding--
# main_domain → domain name (e.g., "software")
# data → {
#    "main": [keywords used to detect this domain],
#    "sub": {
#        "system": [...],
#        "application": [...],
#        "programming": [...]
#    }
# }


#for sub_domain, sub_words in data["sub"].items():
#--Understanding--
# sub_domain → name of the sub-topic inside a domain
#              (e.g., "system", "application", "programming")

# sub_words → list of keywords used to detect that sub-topic
#              (e.g., ["system", "os", "operating system"])