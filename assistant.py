knowledge_base = {
    "software": {
        "system": "System Software: Controls hardware and core operations.",
        "application": "Application Software: Helps users perform tasks.",
        "programming": "Programming Software: Tools like IDEs and compilers."
    },

    "tech": {
        "ai": "Artificial Intelligence: Machines simulating intelligence.",
        "ml": "Machine Learning: Systems that learn from data.",
        "dl": "Deep Learning: Multi-layer neural networks.",
        "nlp": "Natural Language Processing: Understanding human language."
    },

    "database": {
        "sql": "SQL Databases: Structured data.",
        "nosql": "NoSQL Databases: Flexible schema."
    }
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

    elif any(w in text for w in ['database','db','backend']):  

        if any(w in text for w in ['sql','structured query language']):
            return ("database","sql")  
        
        elif any(w in text for w in ['nosql','not only structured query language']):
            return ("database","nosql")  
        
        else:
            return ("database","unknown")

    else:
        return ("unknown","unknown")


def generate_text(intent):

    main_domain, sub_domain = intent

    if main_domain == "software" and sub_domain == "system":
        return knowledge_base["software"]["system"]

    elif main_domain == "software" and sub_domain == "application":
        return knowledge_base["software"]["application"]
    
    elif main_domain == "software" and sub_domain == "programming":
        return knowledge_base["software"]["programming"]
    
    elif main_domain == "software" and sub_domain == "unknown":
        return "Please specify: system, application, or programming software."
    #-------------------------------------------------------------------------------
    elif main_domain == "tech" and sub_domain == "ai":
        return knowledge_base["tech"]["ai"]
    
    elif main_domain == "tech" and sub_domain == "ml":
        return knowledge_base["tech"]["ml"]
        
    elif main_domain == "tech" and sub_domain == "nlp":
        return knowledge_base["tech"]["nlp"]
    
    elif main_domain == "tech" and sub_domain == "dl":
        return knowledge_base["tech"]["dl"]
    
    elif main_domain == "tech" and sub_domain == "unknown":
          return "Please specify: AI, ML, DL, or NLP."
    #-------------------------------------------------------------------------------
    elif main_domain == "database" and sub_domain == "sql":
           return knowledge_base["database"]["sql"]
    
    elif main_domain == "database" and sub_domain == "nosql":
           return knowledge_base["database"]["nosql"]
    
    elif main_domain == "database" and sub_domain == "unknown":
        return "Please specify: Sql or Nosql"
    
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