
import streamlit as st
from app.resume_parser import extract_text_from_pdf
from app.resume_analyzer import analyze_resume
from app.job_scraper import scrape_linkedin_jobs
from app.job_matcher import match_jobs

st.title("💼 AI Resume Analyzer & Career Coach")

resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    st.subheader("Resume Analysis")
    if st.button("Analyze Resume"):
        result = analyze_resume(resume_text)
        st.markdown(result)

    st.subheader("Scrape LinkedIn Jobs")
    if st.button("Find Jobs"):
        jobs = scrape_linkedin_jobs()
        for job in jobs:
            st.write(f"**{job['title']}** at *{job['company']}* - {job['location']}")
            st.markdown(f"[View Job]({job['url']})")

        st.subheader("Job Match Ranking")
        if st.button("Match Jobs"):
            match_result = match_jobs(resume_text, jobs)
            st.markdown(match_result)
