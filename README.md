# 🛡️ Tufin QA Interview Prep — Interactive Quiz App

A polished Streamlit quiz app with **150+ questions across 6 categories**, built to help you ace the **Tufin QA Automation Engineer** interview.

---

## 📋 Table of Contents

- [Features](#features)
- [Categories](#categories)
- [Run Locally](#run-locally)
- [Deploy to Streamlit Cloud](#deploy-to-streamlit-cloud)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)

---

## ✨ Features

- 🎯 **6 categories** covering every topic in the Tufin QA interview
- 🔀 **Randomized questions** every session — no two quizzes are the same
- 📊 **Progress bar** and live question counter
- ✅ **Immediate feedback** after each answer with full explanation
- 📈 **Results page** with score card, emoji rating, and category breakdown
- 🔍 **Review mode** — see every question with correct/incorrect highlighting and filter by result
- 🎨 **Tufin-inspired dark blue theme** with custom CSS
- 🎉 **Confetti animation** when you score 80%+
- 🔢 **Question count selector**: 10 / 15 / 20 / All
- 📚 **Sidebar category filter** — quiz only the topics you need

---

## 📚 Categories

| Category | Questions | Topics |
|---|---|---|
| 🧪 QA Fundamentals | 30 | Test pyramid, bug reports, shift-left, exploratory testing, STAR/FIRMS/SPICED |
| 🌐 Tufin & Networking | 30 | Firewall rules, RBAC, event logs, audit logs, TCP/UDP, IPv4, rate limiting |
| ☕ Java & Debugging | 25 | String comparison, HashMap bugs, ArrayList, loop errors, live coding strategy |
| 🔌 API, SQL & Linux | 25 | HTTP methods, status codes, SQL joins, grep, chmod, stdin/stdout |
| 🔒 Check Point Networking | 10 | Management Server, Security Gateway, Publish → Install lifecycle, SmartLog |
| 🎯 Behavioral & Strategy | 20 | STAR method, PARLA, tell me about yourself, handling unknowns, Tufin mindset |

---

## 🖥️ Run Locally

### Prerequisites

- Python 3.9 or higher
- `pip` package manager

### Step 1 — Clone or download the project

```bash
git clone https://github.com/YOUR_USERNAME/tufin-qa-quiz.git
cd tufin-qa-quiz
```

Or just copy the `quiz_app/` folder to your machine.

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

If you're using a specific Python interpreter (e.g. on Windows):

```bash
C:/Users/WEBDEV/AppData/Local/Python/bin/python.exe -m pip install -r requirements.txt
```

### Step 3 — Run the app

```bash
streamlit run app.py
```

Or with a specific interpreter:

```bash
C:/Users/WEBDEV/AppData/Local/Python/bin/python.exe -m streamlit run app.py
```

The app will open automatically at **http://localhost:8501**

---

## 🚀 Deploy to Streamlit Cloud

Streamlit Community Cloud is **free** and deploys directly from a GitHub repository.

### Step 1 — Push to GitHub

```bash
# Inside the quiz_app/ directory (or repo root)
git init
git add .
git commit -m "Initial commit — Tufin QA Quiz App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tufin-qa-quiz.git
git push -u origin main
```

> ⚠️ Make sure `app.py`, `questions.py`, and `requirements.txt` are all in the **root** of the repository (or note the path for Step 3).

### Step 2 — Sign in to Streamlit Cloud

1. Go to **https://share.streamlit.io**
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your repositories

### Step 3 — Create a new app

1. Click **"New app"** (top right)
2. Fill in the form:

| Field | Value |
|---|---|
| **Repository** | `YOUR_USERNAME/tufin-qa-quiz` |
| **Branch** | `main` |
| **Main file path** | `app.py` *(or `quiz_app/app.py` if nested)* |
| **Python version** | `3.11` (recommended) |
| **App URL** | Choose a custom slug, e.g. `tufin-qa-prep` |

3. Click **"Deploy!"**

Streamlit Cloud will:
- Install packages from `requirements.txt` automatically
- Build and serve the app within ~60 seconds
- Give you a public URL like `https://tufin-qa-prep.streamlit.app`

### Step 4 — Verify deployment

- Open the public URL in your browser
- Confirm all 6 categories load in the sidebar
- Run a quick 10-question quiz to test the full flow

### Updating the app

Any `git push` to `main` will **automatically redeploy** the app on Streamlit Cloud within a minute or two.

```bash
git add .
git commit -m "Update questions or UI"
git push
```

---

## 📁 Project Structure

```
quiz_app/
├── app.py              # Main Streamlit application — all UI & state logic
├── questions.py        # Question bank (150+ questions as a Python list of dicts)
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .gitignore          # Python + Streamlit ignores
```

### Question format

Each question in `questions.py` is a Python dict with this structure:

```python
{
    "question":    "What is the test pyramid?",
    "options":     ["Option A", "Option B", "Option C", "Option D"],
    "answer":      "Option B",          # must exactly match one of the options
    "category":    "QA Fundamentals",   # must match an entry in ALL_CATEGORIES
    "explanation": "Explanation shown after answering.",
}
```

To **add new questions**, simply append dicts in this format to the `QUESTIONS` list in `questions.py`. New categories are picked up automatically.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.9+** | Runtime |
| **Streamlit** | Web UI framework |
| **HTML/CSS** | Custom Tufin-themed styling via `st.markdown` |
| **Session State** | All quiz state managed via `st.session_state` |
| **canvas-confetti** | Celebration animation (CDN, no install needed) |

---

## 🎯 Tips for Using This App

1. **Start focused** — run the quiz with only 1–2 categories at a time to go deep
2. **Review every wrong answer** — the explanations are the most valuable part
3. **Repeat until 80%+** — questions shuffle every run, so repetition builds real recall
4. **Practice the behavioral questions out loud** — reading is not the same as saying it
5. **Time yourself** — aim to answer each question in under 30 seconds

---

## 📄 License

MIT — free to use and modify for personal interview prep.

---

*Built with ❤️ for Tufin QA Automation Engineer interview preparation.*