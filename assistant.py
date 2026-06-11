import random

software_data = {
    "system": "System Software: Controls the core operations of your device, including hardware management, memory, and security.",
    
    "application": "Application Software: Designed to help users perform tasks like browsing, documents, games.",
    
    "programming": "Programming Software: Tools used by developers like IDEs, compilers, debuggers."
}

tech_data = {
    "ai": "Artificial Intelligence: Machines simulating human intelligence.",
    "ml": "Machine Learning: Systems that learn from data (re   commendation systems, spam filters).",
    "dl": "Deep Learning: Neural networks with many layers (image recognition, NLP).",
    "nlp": "Natural Language Processing: Machines understanding human language (chatbots, translation)."
}


def detect_intent(user_input):

    text = user_input.lower()

    if any(w in text for w in ["software","website","application","ios","android"]):
    
        if any(w in text for w in ['system','os','operating system']):
            return ("software","system")
        
        elif any(w in text for w in ['application','app']):
            return ("software","application")
        
        elif any(w in text for w in ['program','programming','coding','code']):
            return ("software","programming")
        
        else:
            return ("software", "unknown")
        
    elif any(w in text for w in ['ai','ml','dl','nlp','technology','tech']):
        
        if any(w in text for w in ['ai','artificial intelligence']):
            return ("tech","ai")
        
        elif any(w in text for w in ['ml','machine learning']):
            return ("tech","ml")    
        
        elif any(w in text for w in ['dl','deep learning']):
            return ("tech","dl")   

        elif any(w in text for w in ['nlp','natural language']):
            return ("tech","nlp")     

        else:
            return ("tech","unknown")

    else:
        return ("unknown","unknown")


def generate_text(intent):

    main_domain , sub_domain = intent

    if main_domain == "software" and sub_domain == "system":
        return software_data["system"]
    
    elif main_domain == "software" and sub_domain == "application":
        return software_data["application"]
    
    elif main_domain == "software" and sub_domain == "programming":
        return software_data["programming"]
    
    elif main_domain == "software" and sub_domain == "unknown":
        return "Please specify: system, application, or programming software."
    
    
    elif main_domain == "tech" and sub_domain == "ai":
        return tech_data["ai"]
    
    elif main_domain == "tech" and sub_domain == "ml":
        return tech_data["ml"]
    
    elif main_domain == "tech" and sub_domain == "dl":
        return tech_data["dl"]
    
    elif main_domain == "tech" and sub_domain == "nlp":
        return tech_data["nlp"]
    
    elif main_domain == "tech" and sub_domain == "unknown":
        return "Please specify: AI, ML, DL, or NLP."

    else:
        return "Data Not Available Yet !"


while True:
    user_input = input("You : ")

    if user_input.lower() == "exit":
        print("Good Bye !")
        break

    intent = detect_intent(user_input)
    result = generate_text(intent)

    print(f"Response -> {result}")