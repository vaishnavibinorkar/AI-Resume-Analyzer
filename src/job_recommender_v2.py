import pdfplumber

skills_db = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "pandas",
    "numpy",
    "excel",
    "power bi"
]

job_roles = {
    "Data Scientist": ["python", "machine learning"],
    "Data Analyst": ["sql", "excel"],
    "Machine Learning Engineer": ["python", "machine learning"],
    "Business Intelligence Analyst": ["sql", "power bi"],
    "Python Developer": ["python"]
}

pdf_path = "uploads/resume.pdf"

text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text.lower()

found_skills = []

for skill in skills_db:
    if skill in text:
        found_skills.append(skill)

print("Skills Found:")
for skill in found_skills:
    print("-", skill)

print("\nRecommended Jobs:")

for job, required_skills in job_roles.items():
    if all(skill in found_skills for skill in required_skills):
        print("-", job)