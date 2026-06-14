import streamlit as st
import pdfplumber

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.sidebar.title("AI Resume Analyzer")
st.sidebar.write("Developed by Vaishnavi")
st.sidebar.write("AI & ML Project")

st.title("📄 AI Resume Analyzer")
st.markdown("### Upload your resume and get AI-powered insights 🚀")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

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

if uploaded_file:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    score = (len(found_skills) / len(skills_db)) * 100

    missing_skills = []

    for skill in skills_db:
        if skill not in found_skills:
            missing_skills.append(skill)

    st.subheader("📊 Resume Score")

    if score >= 80:
        st.success(f"{score:.1f}% - Excellent Resume!")
    elif score >= 60:
        st.warning(f"{score:.1f}% - Good Resume!")
    else:
        st.error(f"{score:.1f}% - Needs Improvement!")

    st.progress(int(score))

    col1, col2, col3 = st.columns(3)

    col1.metric("Skills Found", len(found_skills))
    col2.metric("Missing Skills", len(missing_skills))
    col3.metric("Resume Score", f"{score:.1f}%")

    st.subheader("✅ Skills Found")
    for skill in found_skills:
        st.write(skill.title())

    st.subheader("❌ Missing Skills")
    for skill in missing_skills:
        st.write(skill.title())

    st.subheader("💼 Recommended Jobs")

    for job, required_skills in job_roles.items():
        if all(skill in found_skills for skill in required_skills):
            st.write("✅", job)

    st.subheader("🎯 Career Suggestions")

    if "python" not in found_skills:
        st.write("👉 Learn Python for better opportunities.")

    if "sql" not in found_skills:
        st.write("👉 SQL is important for Data Analyst roles.")

    if "machine learning" not in found_skills:
        st.write("👉 Learn Machine Learning to become a Data Scientist.")

    if len(found_skills) >= 5:
        st.success("🚀 Your profile is strong for internships!")
        