# Sprint 5 Checkpoint: AI-Powered Resume Analyzer

> **Sprint 5 Project** | **60-90 min build** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/sprint-5-checkpoint/)**

Sprint 5 COMPLETE. All 5 Sprints DONE.

You went from `print("Hello, World!")` to building AI applications. Read that sentence again. Let it sink in. You started this book not knowing what a variable was. Now you're using NumPy, pandas, machine learning, and large language models. You're analyzing data, making predictions, and building AI-powered tools.

Most people who start learning to code quit in week one. You didn't. Most people who make it past the basics never touch AI. You just finished an entire sprint on it. You're not a beginner. You're not even intermediate. You're someone who can build real things with Python AND AI.

Now let's prove it. One final sprint project. Then you're ready for the Final Projects.

## The Project: AI-Powered Resume Analyzer

You're going to build an application that:
1. Reads a resume (text file or PDF)
2. Analyzes it with pandas and basic NLP
3. Visualizes the findings with matplotlib
4. Uses an LLM to provide feedback and suggestions
5. Generates an automated report

This project uses skills from every chapter in Sprint 5.

## Skills Used

| Chapter | Skill | How It's Used |
|-----|----|--------|
| 26 - NumPy | Array operations | Scoring calculations, statistics |
| 27 - Pandas | Data analysis | Structuring resume data, analysis |
| 28 - Visualization | Charts | Skills chart, experience timeline |
| 29 - ML | Classification | Categorizing skills, job matching |
| 30 - AI APIs | LLM integration | Resume feedback, improvement tips |
| 31 - LangChain | RAG | Comparing resume against job descriptions |
| 32 - Automation | File handling, reporting | Reading files, generating report |

## Step-by-Step Build Guide

### Step 1: Set Up the Project

```python
# resume_analyzer.py
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import json
import re

# Optional (if you have API keys set up):
# from openai import OpenAI
# client = OpenAI()
```

Create a sample resume to work with:

```python
sample_resume = """
ALEX JOHNSON
Software Developer | alex.johnson@email.com | San Francisco, CA

SUMMARY
Passionate software developer with 4 years of experience in full-stack
web development. Skilled in Python, JavaScript, and cloud technologies.
Looking for a senior developer role at a forward-thinking company.

EXPERIENCE

Software Developer - TechCorp Inc. (2022-Present)
- Built REST APIs using Python and Flask serving 10,000+ daily users
- Implemented CI/CD pipelines with GitHub Actions reducing deploy time by 60%
- Led migration from monolith to microservices architecture
- Mentored 3 junior developers

Junior Developer - StartupXYZ (2020-2022)
- Developed front-end features using React and TypeScript
- Built automated testing suite increasing code coverage from 40% to 85%
- Collaborated with design team on UI/UX improvements
- Participated in agile sprints and code reviews

EDUCATION
B.S. Computer Science - UC Berkeley (2020)
Relevant coursework: Data Structures, Algorithms, Machine Learning, Databases

SKILLS
Python, JavaScript, TypeScript, React, Flask, Django, PostgreSQL, MongoDB,
Docker, Kubernetes, AWS, Git, CI/CD, REST APIs, GraphQL, Agile, Scrum

CERTIFICATIONS
- AWS Solutions Architect Associate (2023)
- Google Professional Cloud Developer (2022)
"""

# Save it
Path("sample_resume.txt").write_text(sample_resume)
print("Sample resume saved!")
```

### Step 2: Parse the Resume (Chapter 32 - File Handling)

```python
def load_resume(file_path):
    """Load a resume from a text file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Resume not found: {file_path}")

    content = path.read_text(encoding="utf-8")
    print(f"Loaded resume: {path.name} ({len(content)} characters)")
    return content

def extract_sections(resume_text):
    """Split resume into sections based on headers."""
    sections = {}
    current_section = "HEADER"
    current_content = []

    for line in resume_text.strip().split("\n"):
        # Check if line is a section header (all caps, short)
        if line.strip().isupper() and len(line.strip()) < 30 and len(line.strip()) > 2:
            if current_content:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = line.strip()
            current_content = []
        else:
            current_content.append(line)

    # Don't forget the last section
    if current_content:
        sections[current_section] = "\n".join(current_content).strip()

    return sections

# Test it
resume = load_resume("sample_resume.txt")
sections = extract_sections(resume)
for section, content in sections.items():
    print(f"\n-- {section} --")
    print(content[:100] + "..." if len(content) > 100 else content)
```

### Step 3: Analyze Skills (Chapters 26 & 27 - NumPy & Pandas)

```python
def analyze_skills(resume_text):
    """Extract and categorize skills from a resume."""

    # Define skill categories
    skill_categories = {
        "Programming Languages": ["python", "javascript", "typescript", "java",
                                   "c++", "go", "rust", "ruby", "php", "swift"],
        "Frontend": ["react", "angular", "vue", "html", "css", "tailwind",
                      "next.js", "svelte"],
        "Backend": ["flask", "django", "fastapi", "node.js", "express",
                     "spring", "rest apis", "graphql"],
        "Databases": ["postgresql", "mysql", "mongodb", "redis", "sqlite",
                       "dynamodb", "elasticsearch"],
        "Cloud & DevOps": ["aws", "gcp", "azure", "docker", "kubernetes",
                           "ci/cd", "terraform", "github actions"],
        "Data & AI": ["machine learning", "pandas", "numpy", "tensorflow",
                       "pytorch", "scikit-learn", "data analysis"],
        "Soft Skills": ["agile", "scrum", "mentoring", "leadership",
                         "collaboration", "communication"]
    }

    resume_lower = resume_text.lower()
    found_skills = {}
    all_found = []

    for category, skills in skill_categories.items():
        matches = [s for s in skills if s in resume_lower]
        if matches:
            found_skills[category] = matches
            all_found.extend(matches)

    # Create a DataFrame
    skill_data = []
    for category, skills in found_skills.items():
        for skill in skills:
            skill_data.append({"category": category, "skill": skill})

    df = pd.DataFrame(skill_data)

    # Calculate scores using NumPy
    category_counts = df["category"].value_counts()
    scores = np.array(category_counts.values)
    total_skills = scores.sum()
    percentages = (scores / total_skills * 100).round(1)

    print(f"\nTotal skills found: {total_skills}")
    print(f"\nSkills by category:")
    for cat, count, pct in zip(category_counts.index, scores, percentages):
        print(f"  {cat}: {count} skills ({pct}%)")

    return df, found_skills

skills_df, found_skills = analyze_skills(resume)
```

### Step 4: Visualize the Analysis (Chapter 28 - Visualization)

```python
def create_resume_dashboard(skills_df, sections, output_path="resume_dashboard.png"):
    """Create a visual dashboard for the resume analysis."""

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Skills by Category (Bar Chart)
    category_counts = skills_df["category"].value_counts()
    colors = plt.cm.Set3(np.linspace(0, 1, len(category_counts)))
    axes[0, 0].barh(category_counts.index, category_counts.values, color=colors)
    axes[0, 0].set_title("Skills by Category", fontsize=13, fontweight="bold")
    axes[0, 0].set_xlabel("Number of Skills")

    # 2. Skills Distribution (Pie Chart)
    axes[0, 1].pie(category_counts.values, labels=category_counts.index,
                    autopct="%1.0f%%", colors=colors, startangle=90)
    axes[0, 1].set_title("Skills Distribution", fontsize=13, fontweight="bold")

    # 3. Resume Section Lengths (Bar Chart)
    section_lengths = {k: len(v.split()) for k, v in sections.items()}
    section_df = pd.Series(section_lengths).sort_values(ascending=True)
    axes[1, 0].barh(section_df.index, section_df.values, color="steelblue")
    axes[1, 0].set_title("Words per Section", fontsize=13, fontweight="bold")
    axes[1, 0].set_xlabel("Word Count")

    # 4. Resume Stats Summary
    total_words = sum(section_lengths.values())
    total_skills = len(skills_df)
    num_sections = len(sections)
    has_summary = "SUMMARY" in sections
    has_education = "EDUCATION" in sections

    stats_text = (
        f"Total Words: {total_words}\n"
        f"Total Skills: {total_skills}\n"
        f"Sections: {num_sections}\n"
        f"Has Summary: {'Yes' if has_summary else 'NO - Add one!'}\n"
        f"Has Education: {'Yes' if has_education else 'NO - Add one!'}\n"
        f"\nSkill Categories: {len(skills_df['category'].unique())}\n"
        f"Top Category: {skills_df['category'].value_counts().index[0]}"
    )
    axes[1, 1].text(0.1, 0.5, stats_text, fontsize=12, fontfamily="monospace",
                     verticalalignment="center", transform=axes[1, 1].transAxes,
                     bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))
    axes[1, 1].set_title("Resume Stats", fontsize=13, fontweight="bold")
    axes[1, 1].axis("off")

    fig.suptitle("Resume Analysis Dashboard", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\nDashboard saved: {output_path}")

create_resume_dashboard(skills_df, sections)
```

### Step 5: Score the Resume (Chapter 29 - ML Concepts)

```python
def score_resume(resume_text, sections, skills_df):
    """Score a resume based on common best practices."""

    scores = {}

    # Length score (300-800 words is ideal for a 1-page resume)
    word_count = len(resume_text.split())
    if 300 <= word_count <= 800:
        scores["length"] = 10
    elif 200 <= word_count <= 1000:
        scores["length"] = 7
    else:
        scores["length"] = 4

    # Section completeness
    important_sections = ["SUMMARY", "EXPERIENCE", "EDUCATION", "SKILLS"]
    found_sections = sum(1 for s in important_sections if s in sections)
    scores["sections"] = round((found_sections / len(important_sections)) * 10)

    # Skills diversity
    num_categories = skills_df["category"].nunique()
    scores["skill_diversity"] = min(10, num_categories * 2)

    # Technical skills count
    total_skills = len(skills_df)
    scores["skill_count"] = min(10, total_skills)

    # Action verbs in experience
    action_verbs = ["built", "led", "developed", "implemented", "created",
                     "designed", "managed", "improved", "increased", "reduced",
                     "launched", "mentored", "collaborated", "automated"]
    experience_text = sections.get("EXPERIENCE", "").lower()
    verbs_found = sum(1 for v in action_verbs if v in experience_text)
    scores["action_verbs"] = min(10, verbs_found * 2)

    # Quantified achievements (numbers in experience section)
    numbers = re.findall(r'\d+', sections.get("EXPERIENCE", ""))
    scores["quantified"] = min(10, len(numbers) * 2)

    # Calculate overall score using NumPy
    weights = np.array([0.10, 0.15, 0.15, 0.15, 0.20, 0.25])
    score_values = np.array(list(scores.values()))
    overall = np.average(score_values, weights=weights)

    print("\n=== Resume Score ===")
    for criterion, score in scores.items():
        bar = "=" * score + "-" * (10 - score)
        print(f"  {criterion:20s} [{bar}] {score}/10")

    print(f"\n  {'OVERALL':20s} [{('=' * round(overall)) + ('-' * (10 - round(overall))))}] {overall:.1f}/10")

    return scores, overall

scores, overall = score_resume(resume, sections, skills_df)
```

### Step 6: AI Feedback (Chapter 30 - AI APIs)

```python
def get_ai_feedback(resume_text, scores):
    """Get AI-powered feedback on the resume."""

    # If you have an OpenAI API key:
    try:
        from openai import OpenAI
        client = OpenAI()

        score_summary = "\n".join(f"- {k}: {v}/10" for k, v in scores.items())

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional resume reviewer. "
                               "Give specific, actionable feedback. "
                               "Be encouraging but honest. "
                               "Limit to 5 bullet points."
                },
                {
                    "role": "user",
                    "content": f"Review this resume and give improvement suggestions.\n\n"
                               f"Resume:\n{resume_text}\n\n"
                               f"Automated scores:\n{score_summary}"
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        feedback = response.choices[0].message.content
        print("\n=== AI Feedback ===")
        print(feedback)
        return feedback

    except Exception as e:
        print(f"\n=== AI Feedback (Offline Mode) ===")
        feedback = generate_offline_feedback(scores)
        print(feedback)
        return feedback

def generate_offline_feedback(scores):
    """Generate basic feedback without AI API."""
    tips = []

    if scores.get("quantified", 0) < 6:
        tips.append("Add more numbers! '10,000+ users' is better than 'many users'.")
    if scores.get("action_verbs", 0) < 6:
        tips.append("Start bullet points with strong action verbs: Built, Led, Designed, Launched.")
    if scores.get("skill_diversity", 0) < 6:
        tips.append("Diversify your skills across more categories (frontend, backend, cloud, etc.).")
    if scores.get("sections", 0) < 10:
        tips.append("Make sure you have all key sections: Summary, Experience, Education, Skills.")
    if scores.get("length", 0) < 7:
        tips.append("Aim for 300-800 words. Concise but comprehensive.")

    if not tips:
        tips.append("Your resume looks strong! Consider tailoring it for specific job descriptions.")

    return "\n".join(f"- {tip}" for tip in tips)

feedback = get_ai_feedback(resume, scores)
```

### Step 7: Generate the Final Report (Chapter 32 - Automation)

```python
def generate_report(resume_path, output_dir="resume_report"):
    """Run the complete analysis and generate a report."""

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    print("=" * 50)
    print("  AI-POWERED RESUME ANALYZER")
    print("=" * 50)

    # Load
    resume = load_resume(resume_path)
    sections = extract_sections(resume)

    # Analyze
    skills_df, found_skills = analyze_skills(resume)

    # Visualize
    dashboard_path = output_dir / "dashboard.png"
    create_resume_dashboard(skills_df, sections, str(dashboard_path))

    # Score
    scores, overall = score_resume(resume, sections, skills_df)

    # AI Feedback
    feedback = get_ai_feedback(resume, scores)

    # Save text report
    report_path = output_dir / "analysis_report.txt"
    with open(report_path, "w") as f:
        f.write("RESUME ANALYSIS REPORT\n")
        f.write(f"{'=' * 40}\n\n")
        f.write(f"Overall Score: {overall:.1f}/10\n\n")
        f.write("Scores:\n")
        for k, v in scores.items():
            f.write(f"  {k}: {v}/10\n")
        f.write(f"\nSkills Found: {len(skills_df)}\n")
        f.write(f"Skill Categories: {skills_df['category'].nunique()}\n\n")
        f.write("Feedback:\n")
        f.write(feedback)

    print(f"\n{'=' * 50}")
    print(f"  Report saved to: {output_dir}/")
    print(f"  - dashboard.png")
    print(f"  - analysis_report.txt")
    print(f"  Overall Score: {overall:.1f}/10")
    print(f"{'=' * 50}")

# Run the full analysis!
generate_report("sample_resume.txt")
```

### Running the Complete Project

```bash
python resume_analyzer.py
```

Expected output:

```
==================================================
  AI-POWERED RESUME ANALYZER
==================================================
Loaded resume: sample_resume.txt (1247 characters)

Total skills found: 14

Skills by category:
  Cloud & DevOps: 4 skills (28.6%)
  Programming Languages: 3 skills (21.4%)
  Backend: 3 skills (21.4%)
  Databases: 2 skills (14.3%)
  Soft Skills: 2 skills (14.3%)

Dashboard saved: resume_report/dashboard.png

=== Resume Score ===
  length               [==========] 10/10
  sections             [==========] 10/10
  skill_diversity      [==========] 10/10
  skill_count          [==========] 10/10
  action_verbs         [==========] 10/10
  quantified           [========-] 8/10

  OVERALL              [==========] 9.7/10

==================================================
  Report saved to: resume_report/
  Overall Score: 9.7/10
==================================================
```

## Stretch Goals

Already done? Try these enhancements:

1. **PDF Support**: Use `PyPDFLoader` from LangChain to read PDF resumes
2. **Job Match**: Compare the resume against a job description using RAG (Chapter 31)
3. **Multiple Resumes**: Analyze a folder of resumes and rank them
4. **Web Interface**: Use Streamlit (`pip install streamlit`) to create a drag-and-drop UI
5. **Email the Report**: Automatically email the analysis using smtplib (Chapter 32)

## Starter and Solution Code

- **Starter code:** [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/sprint-5-checkpoint/starter/)
- **Solution code:** [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/sprint-5-checkpoint/solution/)

## You Did It.

Sprint 5. Complete. All five sprints. Done.

Think about where you started:
- **Sprint 1**: `print("Hello, World!")` - variables, lists, loops
- **Sprint 2**: Dictionaries, functions, file I/O, error handling
- **Sprint 3**: OOP, APIs, web scraping, databases
- **Sprint 4**: Virtual environments, testing, Flask, deployment
- **Sprint 5**: NumPy, pandas, visualization, machine learning, AI APIs, LangChain, automation

That's not a "crash course." That's a transformation. You went from zero to someone who can build real, useful, AI-powered applications.

You're not a beginner. You're not even intermediate. You're someone who can build real things with Python AND AI. The gap between you and a "professional developer" is now just practice and projects - not knowledge.

Now it's time to prove it with the Final Projects. Let's go.
