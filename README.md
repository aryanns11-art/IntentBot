# 🤖 IntentBot

A simple rule-based chatbot built in Python that uses keyword matching and intent detection to answer questions about software, technology, and databases.

This project demonstrates the fundamentals of NLP (Natural Language Processing), intent detection, knowledge representation, and chatbot development without using machine learning models.

---

## ✨ Features

* 🔍 Keyword-based intent detection
* 🧠 Structured knowledge base
* 🎲 Randomized responses
* 💬 Interactive command-line chatbot
* 📚 Covers Software, Technology, and Database topics
* 📝 Beginner-friendly and well-commented code
* 🚀 Easy to extend with new domains and responses

---

## 🏗️ Project Structure

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

### 2️⃣ Intent Detection

The input is converted to lowercase and matched against predefined keywords.

Example:

```text
"ai" → tech → ai
```

### 3️⃣ Knowledge Retrieval

The chatbot identifies the correct domain and sub-domain.

```python
knowledge_base["tech"]["ai"]
```

### 4️⃣ Response Generation

A random response is selected using:

```python
random.choice(...)
```

Example Output:

```text
Bot: AI enables machines to simulate human intelligence.
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/IntentBot.git
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
You: What is AI?
Bot: Artificial Intelligence powers smart systems.

You: Tell me about SQL
Bot: SQL databases store structured data.

You: Explain NLP
Bot: NLP helps machines understand human language.

You: exit
Bot: Goodbye!
```

---

## 🛠️ Technologies Used

* 🐍 Python
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
* Knowledge Bases
* Rule-Based Chatbots
* Basic NLP Concepts
* Python Data Structures

---

## 🔮 Future Improvements

* ✅ Multi-word phrase detection
* ✅ Better intent classification
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
