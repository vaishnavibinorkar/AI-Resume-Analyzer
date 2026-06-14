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

score = (len(found_skills) / len(skills_db)) * 100

print("===== RESUME REPORT =====")
print(f"Resume Score: {score:.1f}%")

print("\nSkills Found:")
for skill in found_skills:
    print("-", skill)
if score >= 80:
    print("\nExcellent Resume!")
elif score >= 60:
    print("\nGood Resume!")
else:
    print("\nNeeds Improvement!")