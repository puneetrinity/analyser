
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_resume(resume_text):
    prompt = f"""
    Analyze this resume. Provide:
    - Summary
    - 3 Strengths
    - 3 Weaknesses
    - Job Title Suggestions
    - Improvement Tips

    Resume:
    {resume_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content
