import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
from pdf2image import convert_from_bytes
import io
import base64
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit Page Config
st.set_page_config(page_title="ATS Resume Score Expert")
st.header("ATS Tracking System")

# File Uploader
uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

# Prompts
input_prompt1 = """
You are an experienced HR with Tech Experience in the field of Data Science, Full Stack
Web Development, Big Data Engineering, DEVOPS, Data Analyst. 
Please review the provided resume and highlight strengths and weaknesses in relation 
to the specified job description.
"""

input_prompt2 = """
You are an HR expert. Provide actionable tips to improve the candidate's resume 
for the roles of Data Science, Web Development, Big Data Engineering, DEVOPS, Data Analyst.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner. Evaluate the resume against 
the provided job description. First provide the percentage match, then list keywords 
missing in the resume.
"""

# Functions
def get_gemini_response(input_prompt, pdf_content, extra_prompt=None):
    model = genai.GenerativeModel('gemini-pro-version')
    combined_input = [input_prompt] + pdf_content
    if extra_prompt:
        combined_input.append(extra_prompt)
    response = model.generate_content(combined_input)
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded.")

    # Convert PDF to images using the correct Poppler path
    poppler_path = r"D:\ML\ML projects\resume analyzer\poppler\Library\bin"

    images = convert_from_bytes(
        uploaded_file.read(),
        poppler_path=poppler_path
    )

    pdf_parts = []
    for page in images:
        img_byte_arr = io.BytesIO()
        page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts.append({
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()
        })

    return pdf_parts, images  # Return both for display

# Buttons
submit1 = st.button("Tell me about the Resume")
submit2 = st.button("How can I Improve my Resume")
submit3 = st.button("Percentage Matched")

# Handle file upload
if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")

    pdf_content, images = input_pdf_setup(uploaded_file)  # Convert all pages

    # Display PDF pages
    st.subheader("Resume Preview")
    for i, page in enumerate(images):
        st.image(page, caption=f"Page {i+1}", use_column_width=True)

    # Button actions
    if submit1:
        response = get_gemini_response(input_prompt1, pdf_content)
        st.subheader("Resume Evaluation")
        st.write(response)

    elif submit2:
        response = get_gemini_response(input_prompt2, pdf_content)
        st.subheader("Improvement Suggestions")
        st.write(response)

    elif submit3:
        response = get_gemini_response(input_prompt3, pdf_content)
        st.subheader("ATS Match Percentage & Missing Keywords")
        st.write(response)

else:
    st.info("Please upload a PDF file to continue.")
