
💼 AI Resume Analyzer & Career Coach

An advanced AI-powered application that analyzes resumes, identifies strengths and weaknesses, suggests job titles, and scrapes relevant jobs from LinkedIn — all using OpenAI and Selenium.

---

🚀 Features

- ✅ Extracts and summarizes resume content using GPT-4
- ✅ Highlights strengths and weaknesses
- ✅ Suggests personalized improvements
- ✅ Recommends job titles based on skills and experience
- ✅ Scrapes LinkedIn for relevant job opportunities
- ✅ Ranks jobs based on resume matching
- ✅ Streamlit interface for interactive use

---

🧠 Powered By

- OpenAI GPT-4
- Selenium
- Streamlit
- PyMuPDF

---

📦 Installation

1. Clone the Repository

   git clone https://github.com/your-username/ai-resume-analyzer.git
   cd ai-resume-analyzer

2. Create .env File

   OPENAI_API_KEY=your_openai_key_here

3. Install Dependencies

   pip install -r requirements.txt

4. Run the Streamlit App

   streamlit run ui/streamlit_app.py

---

📂 Project Structure

ai-resume-analyzer/
├── app/
│   ├── resume_parser.py
│   ├── resume_analyzer.py
│   ├── job_scraper.py
│   └── job_matcher.py
├── ui/
│   └── streamlit_app.py
├── main.py
├── requirements.txt
├── .env
└── README.txt

---

🛡️ License

This project is licensed under the MIT License.
