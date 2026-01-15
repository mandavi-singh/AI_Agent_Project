from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os

DB_NAME = "tasks.db"

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if not os.path.exists(DB_NAME):
        conn = get_db_connection()
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_type TEXT NOT NULL,
                input_text TEXT NOT NULL,
                output_text TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()


# ---- Simple AI Functions ----

def generate_summary(text: str) -> str:
   
    if not text:
        return "No text provided to summarize."
    separators = ".!?\n"
    parts = []
    current = ""
    for ch in text.strip():
        current += ch
        if ch in separators:
            parts.append(current.strip())
            current = ""
            if len(parts) >= 3:
                break
    if not parts:
        parts = [text.strip()]
    bullet_points = "\n".join(f"- {p.strip()}" for p in parts if p.strip())
    return f"Here is a brief summary:\n{bullet_points}"


def generate_todo_list(text: str) -> str:
    if not text:
        return "No tasks provided."
    
    raw = text.replace(" and ", ",")
    candidates = []
    for line in raw.split("\n"):
        for part in line.split(","):
            task = part.strip(" .;:\t")
            if task:
                candidates.append(task)
    if not candidates:
        candidates = [text.strip()]
    todo_lines = "\n".join(f"[ ] {task}" for task in candidates)
    return f"Generated To‑Do List:\n{todo_lines}"


def generate_email_draft(text: str) -> str:
    body = text.strip() or "I hope you are doing well."
    draft = f"""Subject: Regarding your request

Dear Sir/Madam,

{body}

Kindly let me know if there is anything else required from my side.

Thank you and regards,
Mandavi
"""
    return draft


@app.route("/", methods=["GET", "POST"])
def index():
    init_db()
    result = None
    task_type = None
    input_text = ""
    if request.method == "POST":
        task_type = request.form.get("task_type")
        input_text = request.form.get("input_text", "").strip()

        if task_type == "summary":
            result = generate_summary(input_text)
        elif task_type == "todo":
            result = generate_todo_list(input_text)
        elif task_type == "email":
            result = generate_email_draft(input_text)
        else:
            result = "Unknown task type."

        # Save to DB
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO tasks (task_type, input_text, output_text, created_at) VALUES (?, ?, ?, ?)",
            (task_type or "", input_text, result, datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()
        conn.close()

    return render_template("index.html", result=result, selected_task=task_type, input_text=input_text)


@app.route("/history")
def history():
    init_db()
    conn = get_db_connection()
    tasks = conn.execute(
        "SELECT id, task_type, input_text, output_text, created_at FROM tasks ORDER BY id DESC LIMIT 50"
    ).fetchall()
    conn.close()
    return render_template("history.html", tasks=tasks)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, use_reloader=False) 
