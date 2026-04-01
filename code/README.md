# Python Crash Course: From Zero to AI

**Companion code repository** -- every example, exercise, and project from the book, organized by sprint and ready to run.

Whether you have never written a line of code or you are brushing up before diving into AI, this repo has you covered. Clone it, follow along chapter by chapter, and watch your skills stack up.

---

## How to Use This Repository

Each sprint maps to a section of the book. Inside every sprint folder you will find the chapter code, exercises, and a checkpoint project.

| Folder | Sprint | Topics |
|---|---|---|
| `sprint-1/` | **Sprint 1 -- Python Foundations** | Variables, data types, control flow, loops, strings, lists |
| `sprint-2/` | **Sprint 2 -- Core Python** | Functions, dictionaries, file I/O, error handling, modules |
| `sprint-3/` | **Sprint 3 -- Object-Oriented Python** | Classes, inheritance, decorators, generators, comprehensions |
| `sprint-4/` | **Sprint 4 -- Professional Python** | APIs, web scraping, testing, databases, code quality tools |
| `sprint-5/` | **Sprint 5 -- Data Science and AI** | NumPy, Pandas, visualization, ML basics, LLMs, RAG, capstone |

---

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/vinaysolapurkar/python-crash-course.git
cd python-crash-course/code
```

**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

> Sprints 1 through 3 use only the Python standard library, so you can start coding immediately -- no installs required. The `requirements.txt` covers everything you will need from Sprint 4 onward.

---

## Sprint Checkpoint Projects

At the end of each sprint you will build a project that ties together everything you learned. Think of these as mini boss battles.

| Sprint | Checkpoint Project | What You Will Build |
|---|---|---|
| 1 | **Text Adventure Game** | An interactive story driven by user input, conditionals, and loops |
| 2 | **Contact Book CLI** | A command-line app with file persistence and robust error handling |
| 3 | **Inventory Management System** | An OOP-based system with classes, inheritance, and file storage |
| 4 | **Weather Dashboard** | A tested, API-powered app with database storage and clean code |
| 5 | **AI-Powered Data Pipeline** | End-to-end data analysis with visualization and LLM integration |

---

## Final Projects

Ready to go beyond the checkpoints? Pick one (or several) of these capstone projects and make it your own.

1. **Personal Finance Tracker** -- Budget tracking with charts and CSV export
2. **Web Scraper and Analyzer** -- Scrape, store, and visualize data from any site
3. **REST API with Flask** -- Build and deploy your own web API
4. **Machine Learning Predictor** -- Train a model and serve predictions
5. **AI Chatbot** -- Conversational assistant powered by OpenAI or Gemini
6. **RAG Knowledge Base** -- Chat with your own documents using embeddings
7. **Automated Testing Suite** -- Full test coverage for a real-world project
8. **Data Dashboard** -- Interactive Plotly dashboard with live data
9. **CLI Productivity Tool** -- A terminal utility you will actually use every day
10. **Open-Ended Capstone** -- Combine everything and build whatever excites you

---

## Running the Code

Each chapter file can be run on its own:

```bash
python sprint-1/ch01_hello.py
```

For chapters that include exercises, look for the `exercises/` subfolder inside each sprint directory.

---

Happy coding -- and remember, the best way to learn Python is to type every example yourself. No copy-pasting!
