"""
SPRINT 5 CHECKPOINT: AI-Powered Resume Analyzer — SOLUTION
============================================================

This is the grand finale! You've combined:
  - NumPy for number crunching and weighted scoring
  - Pandas for structured data analysis
  - File I/O for reading resumes and saving reports
  - ML-like keyword matching and scoring
  - OpenAI API for intelligent suggestions
  - Email structure for report delivery

You're building AI-powered tools now. That's seriously impressive.
Most "Python beginners" don't get anywhere near this level!
"""

import os
import re
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
from collections import Counter
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gracefully import OpenAI
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Note: openai not installed. AI suggestions will use rule-based fallback.")
    print("Install with: pip install openai\n")


# ============================================================
# SAMPLE RESUME
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
# KEYWORD DICTIONARIES
# ============================================================
TECH_KEYWORDS = {
    "python": 3, "javascript": 3, "typescript": 2, "java": 2,
    "sql": 2, "html": 1, "css": 1, "go": 2, "rust": 2, "c++": 2,
    "react": 2, "django": 2, "flask": 2, "node.js": 2, "express": 1,
    "angular": 2, "vue": 2, "spring": 2, "fastapi": 2,
    "aws": 3, "docker": 3, "kubernetes": 3, "ci/cd": 3,
    "azure": 3, "gcp": 3, "terraform": 3, "jenkins": 2,
    "postgresql": 2, "mongodb": 2, "redis": 2, "mysql": 2,
    "microservices": 2, "rest": 2, "api": 2, "agile": 2,
    "scrum": 2, "git": 2, "testing": 2, "tdd": 2,
    "machine learning": 3, "ai": 3, "deep learning": 3,
    "tensorflow": 3, "pytorch": 3, "nlp": 3, "data science": 3,
}

ACTION_VERBS = {
    "led": 3, "developed": 2, "implemented": 2, "designed": 2,
    "optimized": 3, "built": 2, "created": 2, "managed": 2,
    "improved": 3, "increased": 3, "reduced": 3, "delivered": 2,
    "mentored": 2, "architected": 3, "launched": 3, "automated": 3,
    "collaborated": 1, "maintained": 1, "participated": 1,
}

IMPACT_KEYWORDS = {
    "%": 3, "million": 3, "1m": 3, "users": 2,
    "revenue": 3, "growth": 3, "performance": 2,
    "efficiency": 2, "team": 2, "cross-functional": 2,
}


class ResumeAnalyzer:
    """Analyzes a resume and generates a detailed report."""

    def __init__(self, resume_text):
        self.resume_text = resume_text.strip()
        self.resume_lower = resume_text.lower()
        self.sections = {}
        self.keyword_df = None
        self.verb_df = None
        self.scores = {}
        self.suggestions = ""
        self.report = ""

    # ----------------------------------------------------------
    # TASK 1: Parse the resume into sections
    # ----------------------------------------------------------
    def parse_sections(self):
        """Parse the resume text into sections."""
        # Common section headers
        section_headers = [
            "SUMMARY", "OBJECTIVE", "SKILLS", "EXPERIENCE",
            "EDUCATION", "CERTIFICATIONS", "PROJECTS",
            "AWARDS", "PUBLICATIONS", "VOLUNTEER"
        ]

        lines = self.resume_text.split("\n")
        current_section = "HEADER"
        self.sections = {"HEADER": []}

        for line in lines:
            stripped = line.strip()
            # Check if this line is a section header
            if stripped.upper() in section_headers:
                current_section = stripped.upper()
                self.sections[current_section] = []
            else:
                if current_section not in self.sections:
                    self.sections[current_section] = []
                self.sections[current_section].append(line)

        # Clean up: join lines and strip whitespace
        for section in self.sections:
            self.sections[section] = "\n".join(self.sections[section]).strip()

        print(f"Parsed {len(self.sections)} sections: {list(self.sections.keys())}")
        return self.sections

    # ----------------------------------------------------------
    # TASK 2: Score technical keywords
    # ----------------------------------------------------------
    def score_keywords(self):
        """Score the resume based on technical keywords."""
        results = []
        for keyword, weight in TECH_KEYWORDS.items():
            found = keyword.lower() in self.resume_lower
            results.append({
                "keyword": keyword,
                "found": found,
                "weight": weight,
                "score": weight if found else 0,
            })

        self.keyword_df = pd.DataFrame(results)
        found_count = self.keyword_df["found"].sum()
        total_count = len(self.keyword_df)
        max_score = self.keyword_df["weight"].sum()
        actual_score = self.keyword_df["score"].sum()

        print(f"Keywords: {found_count}/{total_count} found "
              f"(score: {actual_score}/{max_score})")
        return self.keyword_df

    # ----------------------------------------------------------
    # TASK 3: Score action verbs
    # ----------------------------------------------------------
    def score_action_verbs(self):
        """Score action verbs used in the resume."""
        results = []
        # Get words from the resume (simple tokenization)
        words = re.findall(r'\b\w+\b', self.resume_lower)

        for verb, weight in ACTION_VERBS.items():
            count = words.count(verb)
            results.append({
                "verb": verb,
                "count": count,
                "weight": weight,
                "score": min(count, 3) * weight,  # Cap at 3 occurrences
            })

        self.verb_df = pd.DataFrame(results)
        used_verbs = self.verb_df[self.verb_df["count"] > 0]
        print(f"Action verbs: {len(used_verbs)}/{len(ACTION_VERBS)} used")
        return self.verb_df

    # ----------------------------------------------------------
    # TASK 4: Calculate overall score
    # ----------------------------------------------------------
    def calculate_overall_score(self):
        """Calculate overall resume score (0-100)."""

        # --- Technical Keywords Score (40% weight) ---
        max_keyword_score = self.keyword_df["weight"].sum()
        actual_keyword_score = self.keyword_df["score"].sum()
        keyword_pct = (actual_keyword_score / max_keyword_score * 100) if max_keyword_score > 0 else 0

        # --- Action Verb Score (30% weight) ---
        max_verb_score = sum(min(3, 1) * w for w in ACTION_VERBS.values())  # Assuming at least 1 use
        actual_verb_score = self.verb_df["score"].sum()
        verb_pct = min((actual_verb_score / max_verb_score * 100) if max_verb_score > 0 else 0, 100)

        # --- Impact Score (20% weight) ---
        impact_found = 0
        impact_max = len(IMPACT_KEYWORDS)
        for keyword in IMPACT_KEYWORDS:
            if keyword.lower() in self.resume_lower:
                impact_found += 1
        impact_pct = (impact_found / impact_max * 100) if impact_max > 0 else 0

        # --- Completeness Score (10% weight) ---
        expected_sections = {"SUMMARY", "SKILLS", "EXPERIENCE", "EDUCATION"}
        found_sections = set(self.sections.keys()) & expected_sections
        completeness_pct = (len(found_sections) / len(expected_sections) * 100)

        # Check for other good signs
        has_contact = any(c in self.resume_lower for c in ["@", "phone", "linkedin", "github"])
        has_certifications = "CERTIFICATIONS" in self.sections
        has_projects = "PROJECTS" in self.sections
        completeness_pct = min(completeness_pct + (10 if has_contact else 0)
                               + (10 if has_certifications else 0)
                               + (10 if has_projects else 0), 100)

        # --- Weighted Overall Score ---
        weights = np.array([0.40, 0.30, 0.20, 0.10])
        component_scores = np.array([keyword_pct, verb_pct, impact_pct, completeness_pct])
        overall = np.dot(weights, component_scores)
        overall = np.clip(overall, 0, 100)  # Ensure 0-100 range

        # Determine grade
        if overall >= 90:
            grade = "A+"
        elif overall >= 80:
            grade = "A"
        elif overall >= 70:
            grade = "B+"
        elif overall >= 60:
            grade = "B"
        elif overall >= 50:
            grade = "C"
        else:
            grade = "D"

        self.scores = {
            "overall": round(overall, 1),
            "grade": grade,
            "keywords": round(keyword_pct, 1),
            "action_verbs": round(verb_pct, 1),
            "impact": round(impact_pct, 1),
            "completeness": round(completeness_pct, 1),
            "weights": {"keywords": 40, "action_verbs": 30, "impact": 20, "completeness": 10},
        }

        print(f"Overall score: {self.scores['overall']}/100 (Grade: {self.scores['grade']})")
        return self.scores

    # ----------------------------------------------------------
    # TASK 5: Get AI suggestions (with graceful fallback)
    # ----------------------------------------------------------
    def get_ai_suggestions(self):
        """Get improvement suggestions from OpenAI, with fallback."""

        # First, try the AI approach
        api_key = os.getenv("OPENAI_API_KEY")

        if HAS_OPENAI and api_key:
            try:
                client = OpenAI(api_key=api_key)

                # Build a prompt with the analysis results
                prompt = f"""Analyze this resume and provide 5 specific, actionable
improvement suggestions. Be encouraging but honest.

Resume score: {self.scores['overall']}/100 (Grade: {self.scores['grade']})
Keyword coverage: {self.scores['keywords']}%
Action verb strength: {self.scores['action_verbs']}%
Impact metrics: {self.scores['impact']}%
Completeness: {self.scores['completeness']}%

Missing tech keywords: {', '.join(self.keyword_df[~self.keyword_df['found']].head(10)['keyword'].tolist())}

Resume text:
{self.resume_text[:2000]}

Provide exactly 5 suggestions, numbered 1-5. Keep each under 2 sentences.
Focus on what would make the BIGGEST impact."""

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system",
                         "content": "You are an expert resume reviewer and career coach."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.5,
                    max_tokens=500,
                )

                self.suggestions = response.choices[0].message.content
                print("AI suggestions generated!")
                return self.suggestions

            except Exception as e:
                print(f"OpenAI API error: {e}")
                print("Falling back to rule-based suggestions.")

        # Fallback: Rule-based suggestions
        suggestions = []
        suggestions.append("AI-POWERED SUGGESTIONS (rule-based fallback):")
        suggestions.append("(Set OPENAI_API_KEY for personalized AI suggestions!)\n")

        # Missing keywords
        missing = self.keyword_df[~self.keyword_df["found"]]
        high_value_missing = missing[missing["weight"] >= 3]["keyword"].tolist()[:5]
        if high_value_missing:
            suggestions.append(
                f"1. Add these high-value keywords if relevant to your experience: "
                f"{', '.join(high_value_missing)}. "
                f"These are in high demand in tech roles."
            )
        else:
            suggestions.append(
                "1. Great keyword coverage! Consider adding emerging technologies "
                "like AI/ML or cloud-native tools to stay current."
            )

        # Weak action verbs
        weak_verbs = self.verb_df[
            (self.verb_df["count"] > 0) & (self.verb_df["weight"] <= 1)
        ]["verb"].tolist()
        strong_alternatives = ["led", "optimized", "architected", "launched", "automated"]
        if weak_verbs:
            suggestions.append(
                f"2. Replace weak verbs like '{', '.join(weak_verbs[:3])}' with "
                f"stronger alternatives: {', '.join(strong_alternatives[:3])}."
            )
        else:
            suggestions.append(
                "2. Your action verbs are strong! Consider varying them more "
                "to avoid repetition."
            )

        # Impact metrics
        if self.scores["impact"] < 50:
            suggestions.append(
                "3. Add more quantifiable achievements! Use numbers, percentages, "
                "and metrics. Instead of 'improved performance,' say "
                "'improved performance by 40%, reducing load time from 3s to 1.8s.'"
            )
        else:
            suggestions.append(
                "3. Good use of metrics! Try to add metrics to every bullet point — "
                "even rough estimates are better than none."
            )

        # Completeness
        missing_sections = {"SUMMARY", "SKILLS", "EXPERIENCE", "EDUCATION"} - set(self.sections.keys())
        if missing_sections:
            suggestions.append(
                f"4. Add these missing sections: {', '.join(missing_sections)}. "
                f"Recruiters expect to see a complete resume structure."
            )
        else:
            suggestions.append(
                "4. Resume structure is complete! Consider adding a 'Projects' "
                "or 'Certifications' section if you have them."
            )

        # General tip
        word_count = len(self.resume_text.split())
        if word_count < 200:
            suggestions.append(
                f"5. Your resume is only {word_count} words. Aim for 400-600 words "
                f"for a one-page resume. Add more detail to your experience section."
            )
        elif word_count > 800:
            suggestions.append(
                f"5. At {word_count} words, your resume might be too long. "
                f"Aim for a concise one-page format (400-600 words) unless "
                f"you have 10+ years of experience."
            )
        else:
            suggestions.append(
                "5. Resume length is good! Make sure every bullet point "
                "passes the 'so what?' test — does it show impact?"
            )

        self.suggestions = "\n".join(suggestions)
        print("Rule-based suggestions generated (no API key found).")
        return self.suggestions

    # ----------------------------------------------------------
    # TASK 6: Generate the full report
    # ----------------------------------------------------------
    def generate_report(self):
        """Generate a formatted text report."""
        lines = []
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Header
        lines.append("=" * 60)
        lines.append("  RESUME ANALYSIS REPORT")
        lines.append(f"  Generated: {timestamp}")
        lines.append("=" * 60)
        lines.append("")

        # Overall Score
        score = self.scores["overall"]
        grade = self.scores["grade"]
        bar_filled = int(score / 2)  # 50 chars max
        bar = "#" * bar_filled + "-" * (50 - bar_filled)

        lines.append(f"  OVERALL SCORE: {score}/100 (Grade: {grade})")
        lines.append(f"  [{bar}]")
        lines.append("")

        # Score Breakdown
        lines.append("  SCORE BREAKDOWN:")
        lines.append(f"  {'Component':<25s} {'Score':>8s} {'Weight':>8s}")
        lines.append("  " + "-" * 43)

        components = [
            ("Technical Keywords", f"{self.scores['keywords']:.1f}%", "40%"),
            ("Action Verbs", f"{self.scores['action_verbs']:.1f}%", "30%"),
            ("Impact Metrics", f"{self.scores['impact']:.1f}%", "20%"),
            ("Completeness", f"{self.scores['completeness']:.1f}%", "10%"),
        ]
        for name, score_str, weight in components:
            lines.append(f"  {name:<25s} {score_str:>8s} {weight:>8s}")
        lines.append("")

        # Top Keywords Found
        lines.append("  TOP KEYWORDS FOUND:")
        found_keywords = self.keyword_df[self.keyword_df["found"]].sort_values(
            "weight", ascending=False
        ).head(10)
        for _, row in found_keywords.iterrows():
            stars = "*" * row["weight"]
            lines.append(f"    {row['keyword']:<20s} (value: {stars})")
        lines.append("")

        # Missing High-Value Keywords
        missing_high = self.keyword_df[
            (~self.keyword_df["found"]) & (self.keyword_df["weight"] >= 3)
        ]
        if len(missing_high) > 0:
            lines.append("  MISSING HIGH-VALUE KEYWORDS:")
            for _, row in missing_high.head(8).iterrows():
                lines.append(f"    - {row['keyword']} (weight: {row['weight']})")
            lines.append("")

        # Action Verbs Analysis
        lines.append("  ACTION VERBS USED:")
        used_verbs = self.verb_df[self.verb_df["count"] > 0].sort_values(
            "score", ascending=False
        )
        for _, row in used_verbs.iterrows():
            strength = "STRONG" if row["weight"] >= 3 else ("GOOD" if row["weight"] >= 2 else "WEAK")
            lines.append(f"    {row['verb']:<15s} (used {row['count']}x, strength: {strength})")
        lines.append("")

        # Sections Found
        lines.append("  RESUME SECTIONS:")
        expected = ["SUMMARY", "SKILLS", "EXPERIENCE", "EDUCATION",
                     "CERTIFICATIONS", "PROJECTS"]
        for section in expected:
            status = "FOUND" if section in self.sections else "MISSING"
            icon = "[+]" if status == "FOUND" else "[-]"
            lines.append(f"    {icon} {section}")
        lines.append("")

        # Suggestions
        lines.append("-" * 60)
        lines.append("  IMPROVEMENT SUGGESTIONS")
        lines.append("-" * 60)
        lines.append("")
        for line in self.suggestions.split("\n"):
            lines.append(f"  {line}")
        lines.append("")

        # Footer
        lines.append("=" * 60)
        lines.append("  Keep improving! Every revision makes your resume stronger.")
        lines.append("  Remember: Your resume is a living document, not a tombstone.")
        lines.append("=" * 60)

        self.report = "\n".join(lines)
        return self.report

    # ----------------------------------------------------------
    # TASK 7: Email the report (structure only)
    # ----------------------------------------------------------
    def email_report(self, to_email):
        """Show the email structure for sending the report."""
        sender = os.getenv("GMAIL_ADDRESS")
        password = os.getenv("GMAIL_APP_PASSWORD")

        print(f"\n{'=' * 60}")
        print("  EMAIL REPORT")
        print(f"{'=' * 60}")

        if not sender or not password:
            print(f"""
  [DEMO MODE] Email that would be sent:

  From:    your-email@gmail.com
  To:      {to_email}
  Subject: Resume Analysis Report - {datetime.now().strftime('%Y-%m-%d')}

  Body:
  {self.report[:300]}...

  To actually send emails, set environment variables:
    GMAIL_ADDRESS=your-email@gmail.com
    GMAIL_APP_PASSWORD=your-app-password

  (You need a Gmail App Password, not your regular password.
   Go to: Google Account > Security > 2-Step Verification > App Passwords)
""")
            return False

        try:
            msg = MIMEMultipart()
            msg["From"] = sender
            msg["To"] = to_email
            msg["Subject"] = f"Resume Analysis Report - {datetime.now().strftime('%Y-%m-%d')}"
            msg.attach(MIMEText(self.report, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(msg)

            print(f"  Report emailed to {to_email}!")
            return True
        except Exception as e:
            print(f"  Failed to send email: {e}")
            return False

    # ----------------------------------------------------------
    # TASK 8: Run the full analysis
    # ----------------------------------------------------------
    def analyze(self):
        """Run all analysis steps and return the report."""
        print("\n" + "=" * 60)
        print("  ANALYZING RESUME...")
        print("=" * 60 + "\n")

        print("Step 1/6: Parsing sections...")
        self.parse_sections()

        print("Step 2/6: Scoring technical keywords...")
        self.score_keywords()

        print("Step 3/6: Analyzing action verbs...")
        self.score_action_verbs()

        print("Step 4/6: Calculating overall score...")
        self.calculate_overall_score()

        print("Step 5/6: Generating suggestions...")
        self.get_ai_suggestions()

        print("Step 6/6: Building report...")
        self.generate_report()

        print("\nAnalysis complete!\n")
        return self.report


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  AI-POWERED RESUME ANALYZER")
    print("  Sprint 5 Checkpoint Project")
    print("=" * 60)

    # Step 1: Save sample resume to a file
    base_dir = Path(__file__).parent.resolve()
    resume_file = base_dir / "sample_resume.txt"
    resume_file.write_text(SAMPLE_RESUME.strip())
    print(f"\nSample resume saved to: {resume_file}")

    # Step 2: Read the resume from file (just like a real app would)
    resume_text = resume_file.read_text()
    print(f"Resume loaded: {len(resume_text)} characters, {len(resume_text.split())} words")

    # Step 3: Create analyzer and run
    analyzer = ResumeAnalyzer(resume_text)
    report = analyzer.analyze()

    # Step 4: Print the report
    print(report)

    # Step 5: Save the report
    report_file = base_dir / "resume_report.txt"
    report_file.write_text(report)
    print(f"\nReport saved to: {report_file}")

    # Step 6: Show email structure
    analyzer.email_report("candidate@example.com")

    # Bonus: Show the pandas DataFrames
    print("\n" + "=" * 60)
    print("  DETAILED DATA (Pandas DataFrames)")
    print("=" * 60)
    print("\nKeyword Analysis (top 15):")
    print(analyzer.keyword_df.sort_values("score", ascending=False).head(15).to_string(index=False))
    print("\nAction Verb Analysis:")
    print(analyzer.verb_df[analyzer.verb_df["count"] > 0].sort_values(
        "score", ascending=False).to_string(index=False))

    print("\n" + "=" * 60)
    print("  SPRINT 5 COMPLETE!")
    print("=" * 60)
    print("""
You've just built an AI-powered application that:

  1. Reads files from disk (Chapter 32)
  2. Structures data with Pandas (Chapter 27)
  3. Crunches numbers with NumPy (Chapter 26)
  4. Applies ML-like scoring algorithms (Chapter 29)
  5. Connects to AI APIs for suggestions (Chapter 30)
  6. Generates professional reports
  7. Can email results automatically (Chapter 32)

That's not normal beginner stuff. You've leveled up!

Next steps in your journey:
  - Build a web app with Flask/Django
  - Deploy to the cloud (AWS/GCP/Azure)
  - Contribute to open source
  - Build your own AI-powered projects!

Happy coding! The world needs more Python developers like you!
""")
