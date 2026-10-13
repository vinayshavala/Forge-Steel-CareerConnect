import streamlit as st
import PyPDF2
import re
import numpy as np
from sentence_transformers import SentenceTransformer, util

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + " "
    return text

# ---------------- TEXT CLEANING ----------------
def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9., ]", " ", text)
    return " ".join(text.split())

# ---------------- ATS SEMANTIC MATCH ----------------
def ats_match(job_desc, resume_text):
    jd_emb = model.encode(job_desc, convert_to_tensor=True)
    resume_emb = model.encode(resume_text, convert_to_tensor=True)

    similarity = util.cos_sim(jd_emb, resume_emb)[0][0].item()
    return round(similarity * 100, 2)

# ---------------- MISSING KEYWORDS ----------------
def find_missing_keywords(job_desc, resume_text):
    jd_words = {w.lower() for w in job_desc.split() if len(w) > 3}
    resume_words = {w.lower() for w in resume_text.split() if len(w) > 3}
    return list(jd_words - resume_words)[:15]

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="ATS Resume Scanner")
st.title("📄 ATS Resume Scanner")
st.caption("Semantic Matching • Sentence Transformers • 100% Free")

job_desc = st.text_area("📝 Job Description", height=200)
uploaded_file = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])

if st.button("🚀 Analyze Resume"):
    if uploaded_file and job_desc:
        resume_text = clean_text(extract_text_from_pdf(uploaded_file))
        job_desc = clean_text(job_desc)

        score = ats_match(job_desc, resume_text)
        missing = find_missing_keywords(job_desc, resume_text)

        st.subheader("📊 ATS Match Score")
        st.progress(score / 100)
        st.write(f"**Match Percentage:** {score}%")

        st.subheader("❌ Missing / Weak Keywords")
        st.write(", ".join(missing))

        st.subheader("✅ ATS Verdict")
        if score >= 75:
            st.success("Strong ATS Compatibility")
        elif score >= 55:
            st.warning("Moderate ATS Compatibility")
        else:
            st.error("Low ATS Compatibility")
    else:
        st.warning("Please upload resume and enter job description")
