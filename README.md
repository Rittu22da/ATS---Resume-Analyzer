📝 ATS Resume Analyzer


An AI-powered Resume Evaluation System built with Streamlit and Google Gemini that analyzes your resume against any job description and provides detailed feedback, skill-gap analysis, and ATS (Applicant Tracking System) match score.

🚀 Key Features

Resume Parsing: Upload your resume in PDF format — the system automatically extracts text and relevant content.

Job Description Matching: Compares your resume with the job role to evaluate suitability.

ATS Score Calculation: Provides a percentage match score based on skills and role requirements.

Strength & Weakness Insights: Highlights strong points and areas to improve.

Missing Keywords Detection: Identifies required skills or keywords not covered in the resume.

Actionable Improvement Suggestions: Helps optimize your resume for ATS & HR screening.

🛠️ Tech Stack
Component	Technology Used
Frontend / UI	Streamlit
AI Model	Google Gemini API
File Processing	pdf2image, Pillow (PIL)
Environment Management	python-dotenv
📦 How It Works

Upload your resume (PDF format).

Paste the job description of the role you're targeting.

The system processes the resume and job description.

View your:

✅ Resume Evaluation

🎯 ATS Match Score

🔑 Missing Skills & Keywords

📌 Improvement Suggestions

📷 Example UI
ATS Analyzing System
| Upload Resume | Enter Job Description | Analyze |

📁 File Structure
├── app.py                     # Streamlit main application
├── import streamlit as st.py  # Alternative implementation
├── test.py                    # Model testing script (optional)
├── requirements.txt           # Required dependencies
└── README.md                  # Project documentation

⚙️ Setup Instructions
git clone <your-repo-link>
cd <repo-folder>

pip install -r requirements.txt

# Add your API key in .env
GOOGLE_API_KEY=your_api_key_here

streamlit run app.py
