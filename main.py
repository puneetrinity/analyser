
from app.resume_parser import extract_text_from_pdf
from app.resume_analyzer import analyze_resume

with open("your_resume.pdf", "rb") as f:
    text = extract_text_from_pdf(f)
    analysis = analyze_resume(text)
    print(analysis)
