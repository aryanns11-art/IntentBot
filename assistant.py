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
        "main": ["database","db","backend"],
        "sub": {
            "sql": ["sql","structured query language"],
            "nosql": ["nosql","mongodb","firebase"]
        }
    }
}


def detect_intent(user_input):
    text = user_input.lower()
        
    for main_domain, data in keywords.items():  # go bottom of code to understand

        if any(word in text for word in data["main"]):

            for sub_domain, sub_words in data["sub"].items():

                if any(word in text for word in sub_words):
                    return (main_domain, sub_domain)

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


# main_domain → domain name (e.g., "software")
# data → {
#    "main": [keywords used to detect this domain],
#    "sub": {
#        "system": [...],
#        "application": [...],
#        "programming": [...]
#    }
# }