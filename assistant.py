import random

knowledge_base = { 
    "software": {
        "system": [
            "System Software controls hardware and core operations.",
            "OS and system tools manage your computer resources.",
            "System software acts as a bridge between hardware and user."
        ],
        "application": [
            "Application software helps users perform tasks.",
            "Apps like browsers and editors are application software.",
            "These programs are designed for end users."
        ],
        "programming": [
            "Programming software includes IDEs and compilers.",
            "Developers use tools like VS Code or PyCharm.",
            "These tools help in writing and debugging code."
        ]
    },

    "tech": {
        "ai": [
            "AI enables machines to simulate human intelligence.",
            "Artificial Intelligence powers smart systems.",
            "AI is used in automation and decision-making."
        ],
        "ml": [
            "Machine Learning allows systems to learn from data.",
            "ML models improve with experience.",
            "It is a subset of AI."
        ],
        "dl": [
            "Deep Learning uses neural networks.",
            "DL handles complex patterns like images and speech.",
            "It is an advanced form of ML."
        ],
        "nlp": [
            "NLP helps machines understand human language.",
            "Chatbots use NLP to communicate.",
            "It deals with text and speech processing."
        ]
    },

    "database": {
        "sql": [
            "SQL databases store structured data.",
            "They use tables and relationships.",
            "Examples include MySQL and PostgreSQL."
        ],
        "nosql": [
            "NoSQL databases have flexible schemas.",
            "They store unstructured data.",
            "Examples include MongoDB and Firebase."
        ]
    }
}


keywords = {
    "software": {
        "main": ["software","app","application","program","ios","android","windows"],
        "sub": {
            "system": ["system","os","operating system"],
            "application": ["application","app"],
            "programming": ["programming","coding","code","developer"]
        }
    },

    "tech": {
        "main": ["tech","technology","ai","ml","dl","nlp"],
        "sub": {
            "ai": ["ai","artificial intelligence"],
            "ml": ["ml","machine learning"],
            "dl": ["dl","deep learning"],
            "nlp": ["nlp","natural language","chatbot"]
        }
    },

    "database": {
        "main": ["database","db","backend","sql","mysql"],
        "sub": {
            "sql": ["sql","structured query language"],
            "nosql": ["nosql","mongodb","firebase"]
        }
    }
}


def detect_intent(user_input):
    text = user_input.lower()
    words = text.split()

    for main_domain, data in keywords.items(): # Go bottom for understanding

        if any(word in words for word in data["main"]):

            for sub_domain, sub_words in data["sub"].items():

                if any(word in words for word in sub_words):
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

    return ("unknown","unknown")


def generate_text(intent):
    main_domain, sub_domain = intent

    if main_domain in knowledge_base:

        if sub_domain in knowledge_base[main_domain]:
            return random.choice(knowledge_base[main_domain][sub_domain])

        else:
            return f"Please specify a sub-domain for {main_domain}."

    return "Data Not Available Yet!"


def chatbot():
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        intent = detect_intent(user_input)
        response = generate_text(intent)

        print(f"Bot: {response}")


chatbot()

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