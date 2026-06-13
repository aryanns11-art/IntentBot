# 🤖 IntentBot

A rule-based chatbot built in Python that uses keyword matching and intent detection to answer questions about Software, Technology, and Database concepts.

Unlike simple FAQ bots, IntentBot supports topic classification, sub-topic selection, follow-up questions, contextual conversations, and external JSON-based knowledge storage.

This project demonstrates the fundamentals of NLP (Natural Language Processing), intent detection, knowledge representation, and chatbot development without using machine learning models.

---

## ✨ Features

* 🔍 Keyword-based intent detection
* 🧠 Structured knowledge base stored in JSON
* 🎲 Randomized responses for natural interactions
* 💬 Interactive command-line chatbot
* 📚 Covers Software, Technology, and Database topics
* 🗂️ Domain and sub-domain classification
* 📝 Follow-up questions and explanations
* 🧠 Context memory for continuing conversations
* 📖 Example-based learning responses
* ⚠️ Graceful handling of unknown topics
* 🚀 Easy to extend with new domains and responses

---

## 🏗️ Project Structure

```text
IntentBot/
│
├── chatbot.py
├── data-sets.json
└── README.md
```

### Knowledge Base Structure

```text
Knowledge Base
│
├── Software
│   ├── System
│   ├── Application
│   └── Programming
│
├── Technology
│   ├── AI
│   ├── ML
│   ├── DL
│   └── NLP
│
└── Database
    ├── SQL
    └── NoSQL
```

---

## ⚙️ How It Works

### 1️⃣ User Input

The chatbot accepts a message from the user.

```text
You: Tell me about AI
```

---

### 2️⃣ Intent Detection

The input is converted to lowercase and matched against predefined keywords.

Example:

```text
"ai" → tech → ai
```

The chatbot identifies:

* Main Domain
* Sub-Domain

Example:

```python
("tech", "ai")
```

---

### 3️⃣ Sub-Topic Selection

If a main topic is detected but no specific sub-topic is found, the chatbot asks the user to choose one.

Example:

```text
You: Tell me about technology

Bot: Main topic found: tech
Please choose a sub-topic:

1. ai
2. ml
3. dl
4. nlp
```

---

### 4️⃣ Knowledge Retrieval

The chatbot retrieves information from the JSON knowledge base.

```python
knowledge_base["tech"]["ai"]
```

---

### 5️⃣ Response Generation

A random response is selected to make conversations feel less repetitive.

```python
random.choice(...)
```

Example Output:

```text
Bot: AI enables machines to simulate human intelligence.
```

---

### 6️⃣ Follow-Up Conversations

After answering, the chatbot can offer additional explanations or examples.

Example:

```text
Bot: AI enables machines to simulate human intelligence.

Bot: Do you want examples?
You: yes

Bot: ChatGPT and recommendation systems are examples of AI applications.
```

---

### 7️⃣ Context Memory

The chatbot remembers the last valid topic discussed.

Example:

```text
You: Tell me about AI
Bot: AI enables machines to simulate human intelligence.

You: Give examples
Bot: ChatGPT and recommendation systems are examples of AI applications.
```

This creates a more natural conversational experience.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/aryanns11-art/IntentBot.git
```

Navigate to the project folder:

```bash
cd IntentBot
```

Run the chatbot:

```bash
python chatbot.py
```

---

## 💡 Example Usage

```text
You: Tell me about AI
Bot: Artificial Intelligence powers smart systems.

Bot: Want me to explain more?
You: yes

Bot: AI enables machines to perform tasks that normally require human intelligence.

You: Give examples
Bot: ChatGPT and virtual assistants are examples of AI applications.

You: Tell me about SQL
Bot: SQL databases store structured data.

You: exit
Bot: Goodbye!
```

---

## 🛠️ Technologies Used

* 🐍 Python
* 📄 JSON
* 📖 Dictionaries
* 🔄 Loops
* ⚡ Functions
* 🎯 Conditional Statements
* 🎲 Random Module

---

## 🎓 Learning Objectives

This project helps beginners understand:

* Intent Detection
* Keyword Matching
* Rule-Based Chatbots
* Knowledge Representation
* JSON Data Handling
* Basic NLP Concepts
* Python Data Structures
* Conversational Flow Design

---

## 🔮 Future Improvements

* ✅ Better keyword matching
* ✅ Intent scoring system
* ✅ Multi-domain query handling
* ✅ Context-aware conversations
* ✅ GUI using Tkinter / CustomTkinter
* ✅ Database integration
* ✅ Machine Learning based intent detection
* ✅ Voice-enabled chatbot

---

## 👨‍💻 Author

**Aryan Gavade**

Python • NLP • AI Enthusiast

---

## ⭐ Support

If you found this project helpful, consider giving it a **star ⭐** on GitHub!
