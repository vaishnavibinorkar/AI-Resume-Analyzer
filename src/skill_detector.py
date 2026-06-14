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