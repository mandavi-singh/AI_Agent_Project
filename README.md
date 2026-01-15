# AI Agent Project – Task-Based Productivity App

This project is a task-based productivity web application built using **Flask** and **SQLite**.  
It is designed as a clean and stable prototype that can later be extended into an AI-powered agent.

---

## 🚀 Features

The application supports three main tasks:

### 1. Text Summary
- Converts long paragraphs into short, readable bullet points
- Useful for notes, articles, and study material

### 2. To-Do List Generator
- Converts tasks written in plain text into a structured checklist
- Helps in task planning and productivity

### 3. Email Draft Generator
- Generates a professional email from simple user input
- Useful for academic or formal communication

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Version Control:** Git & GitHub

---

## 🗂 Project Structure
AI_Agent_Project/

│

├── ai_agent_project/

│ ├── app.py

│ ├── templates/

│ │ ├── index.html

│ │ └── history.html

│ └── static/

│ └── style.css
│
├── .gitignore

└── README.md

---

## 📌 How It Works

1. User selects a task type (Summary / To-Do / Email)
2. User enters text input
3. The backend processes the input using rule-based logic
4. Output is displayed on the screen
5. All inputs and outputs are stored in a SQLite database for history tracking

---

## 🧠 Why Rule-Based (No AI Yet)?

This project intentionally uses **rule-based logic** in the initial phase to ensure:
- Stability
- Speed
- No dependency on external APIs
- Clear and modular system design

This makes the application a strong **base prototype**.

---

## 🔮 Future Scope

- Integration of AI models for smarter summarization
- RAG-based chatbot using documents
- Agent-based intelligence for task automation
- Support for multiple LLMs (OpenAI / Gemini)

---

## ▶️ How to Run Locally

```bash
# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install flask

# Run the app
python app.py

