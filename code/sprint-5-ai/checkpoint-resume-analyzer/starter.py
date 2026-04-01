"""
SPRINT 5 CHECKPOINT: AI-Powered Resume Analyzer
=================================================

Congratulations! You've made it to the final checkpoint!

You're going to build a resume analyzer that combines EVERYTHING
you've learned in Sprint 5:
  - NumPy for number crunching
  - Pandas for structured data
  - File operations for reading resumes
  - ML-like keyword scoring
  - OpenAI API for improvement suggestions (optional)
  - Report generation

This is a real-world project! Resume analyzers are used by:
  - Job seekers to improve their resumes
  - Recruiters to screen candidates
  - Career coaches to give feedback

THE SYSTEM WILL:
1. Read a resume from a text file
2. Parse and structure the data with pandas
3. Score the resume based on keywords (ML-like scoring)
4. Use OpenAI API to generate improvement suggestions (with fallback)
5. Generate a formatted report
6. Optionally email the report

REQUIREMENTS:
  pip install numpy pandas openai

OPTIONAL:
  Set OPENAI_API_KEY environment variable for AI suggestions

STRUCTURE:
  - ResumeAnalyzer class with methods for each step
  - Main function that orchestrates the analysis
  - Graceful fallback when API keys are missing

TASKS:
  Fill in each TODO section below. The code skeleton is provided.
  Follow the comments for guidance!
"""

import os
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
from collections import Counter

# Try to import OpenAI (gracefully handle if not installed)
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


# ============================================================
# SAMPLE RESUME (saved as a text file)
# ============================================================
SAMPLE_RESUME = """
JANE DOE
jane.doe@email.com | (555) 123-4567 | linkedin.com/in/janedoe | github.com/janedoe

SUMMARY
Passionate software engineer with 5 years of experience in full-stack development.
Skilled in Python, JavaScript, and cloud technologies. Strong problem-solving abilities
and excellent communication skills. Led a team of 4 developers to deliver projects on time.

SKILLS
Programming: Python, JavaScript, TypeScript, SQL, HTML, CSS
Frameworks: React, Django, Flask, Node.js, Express
Cloud: AWS (EC2, S3, Lambda), Docker, Kubernetes
Tools: Git, CI/CD, Jenkins, PostgreSQL, MongoDB, Redis
Soft Skills: Team leadership, Agile/Scrum, Communication, Problem-solving

EXPERIENCE
Senior Software Engineer | TechCorp Inc. | 2021 - Present
- Led development of microservices architecture serving 1M+ users
- Implemented CI/CD pipelines reducing deployment time by 60%
- Mentored 3 junior developers and conducted code reviews
- Optimized database queries resulting in 40% performance improvement

Software Engineer | StartupXYZ | 2019 - 2021
- Built RESTful APIs using Python/Django for mobile app backend
- Developed real-time notification system using WebSockets
- Collaborated with cross-functional teams in Agile environment
- Increased test coverage from 45% to 85%

Junior Developer | WebAgency Co. | 2018 - 2019
- Created responsive web applications using React and Node.js
- Maintained and debugged legacy PHP applications
- Participated in daily standups and sprint planning

EDUCATION
Bachelor of Science in Computer Science | State University | 2018
GPA: 3.7/4.0 | Relevant Coursework: Data Structures, Algorithms, Databases

CERTIFICATIONS
- AWS Certified Solutions Architect
- Google Professional Cloud Developer

PROJECTS
- Open-source Python package for data validation (500+ GitHub stars)
- Personal blog with 10K monthly visitors built with Next.js
"""


# ============================================================
# KEYWORD DICTIONARIES (for scoring)
# ============================================================
# These are weighted keywords that indicate resume strength.
# Higher weight = more important for a tech role.

TECH_KEYWORDS = {
    # Programming Languages (weight: 3)
    "python": 3, "javascript": 3, "typescript": 2, "java": 2,
    "sql": 2, "html": 1, "css": 1, "go": 2, "rust": 2, "c++": 2,

    # Frameworks (weight: 2)
    "react": 2, "django": 2, "flask": 2, "node.js": 2, "express": 1,
    "angular": 2, "vue": 2, "spring": 2, "fastapi": 2,

    # Cloud & DevOps (weight: 3)
    "aws": 3, "docker": 3, "kubernetes": 3, "ci/cd": 3,
    "azure": 3, "gcp": 3, "terraform": 3, "jenkins": 2,

    # Databases (weight: 2)
    "postgresql": 2, "mongodb": 2, "redis": 2, "mysql": 2,

    # Concepts (weight: 2)
    "microservices": 2, "rest": 2, "api": 2, "agile": 2,
    "scrum": 2, "git": 2, "testing": 2, "tdd": 2,

    # AI/ML (weight: 3 — hot topic!)
    "machine learning": 3, "ai": 3, "deep learning": 3,
    "tensorflow": 3, "pytorch": 3, "nlp": 3, "data science": 3,
}

ACTION_VERBS = {
    # Strong action verbs get higher weights
    "led": 3, "developed": 2, "implemented": 2, "designed": 2,
    "optimized": 3, "built": 2, "created": 2, "managed": 2,
    "improved": 3, "increased": 3, "reduced": 3, "delivered": 2,
    "mentored": 2, "architected": 3, "launched": 3, "automated": 3,
    "collaborated": 1, "maintained": 1, "participated": 1,
}

IMPACT_KEYWORDS = {
    # Words that show measurable impact
    "%": 3, "million": 3, "1m": 3, "users": 2,
    "revenue": 3, "growth": 3, "performance": 2,
    "efficiency": 2, "team": 2, "cross-functional": 2,
}


class ResumeAnalyzer:
    """Analyzes a resume and generates a detailed report."""

    def __init__(self, resume_text):
        self.resume_text = resume_text
        self.resume_lower = resume_text.lower()
        self.scores = {}
        self.report = ""

    # TODO 1: Parse the resume into sections
    def parse_sections(self):
        """
        Parse the resume text into sections (Summary, Skills, Experience, etc.)
        Returns a dictionary of {section_name: section_content}

        Hint: Split by known section headers. Look for lines that are
        ALL CAPS (like "SUMMARY", "SKILLS", "EXPERIENCE", etc.)
        """
        pass

    # TODO 2: Score technical keywords
    def score_keywords(self):
        """
        Score the resume based on technical keywords found.
        Returns a pandas DataFrame with keyword, found (bool), weight.

        Hint: For each keyword in TECH_KEYWORDS, check if it's in
        self.resume_lower. Create a DataFrame with the results.
        """
        pass

    # TODO 3: Score action verbs
    def score_action_verbs(self):
        """
        Score the resume based on action verbs used.
        Returns a pandas DataFrame with verb, count, weight.

        Hint: Count how many times each verb appears in the resume.
        Use the ACTION_VERBS dictionary.
        """
        pass

    # TODO 4: Calculate overall score
    def calculate_overall_score(self):
        """
        Calculate an overall resume score (0-100) based on:
        - Technical keyword coverage (40%)
        - Action verb strength (30%)
        - Impact/metrics presence (20%)
        - Length/completeness (10%)

        Use numpy for the weighted calculation!

        Store results in self.scores dictionary.
        """
        pass

    # TODO 5: Get AI suggestions (with graceful fallback)
    def get_ai_suggestions(self):
        """
        Use OpenAI API to generate improvement suggestions.
        If API is not available, return rule-based suggestions.

        Hint: Send the resume + score breakdown to GPT and ask for
        specific, actionable improvement suggestions.
        Use try/except to handle missing API key!
        """
        pass

    # TODO 6: Generate the full report
    def generate_report(self):
        """
        Generate a formatted text report with:
        - Overall score and grade
        - Section-by-section analysis
        - Top strengths
        - Areas for improvement
        - AI-powered suggestions (if available)

        Returns the report as a string.
        """
        pass

    # TODO 7: Optionally email the report
    def email_report(self, to_email):
        """
        Show the structure for emailing the report.
        (Don't actually send — just show the email that WOULD be sent.)

        Use smtplib structure from Chapter 32.
        """
        pass

    # TODO 8: Run the full analysis
    def analyze(self):
        """
        Run all analysis steps and return the report.
        This is the main method that orchestrates everything.
        """
        # 1. Parse sections
        # 2. Score keywords
        # 3. Score action verbs
        # 4. Calculate overall score
        # 5. Get AI suggestions
        # 6. Generate report
        # 7. Return report
        pass


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    # Step 1: Save sample resume to a file
    resume_file = Path(__file__).parent / "sample_resume.txt"
    resume_file.write_text(SAMPLE_RESUME.strip())
    print(f"Sample resume saved to: {resume_file}")

    # Step 2: Read the resume
    resume_text = resume_file.read_text()

    # Step 3: Create analyzer and run analysis
    analyzer = ResumeAnalyzer(resume_text)
    report = analyzer.analyze()

    # Step 4: Print the report
    print(report)

    # Step 5: Save the report
    report_file = Path(__file__).parent / "resume_report.txt"
    report_file.write_text(report)
    print(f"\nReport saved to: {report_file}")

    # Step 6 (Optional): Email the report
    # analyzer.email_report("candidate@email.com")
