import streamlit as st
import requests
import markdown
from markupsafe import Markup
import fitz  # PyMuPDF

CLOUD_FUNCTION_URL = 'https://resumatch-backend-790682135616.us-west1.run.app'

st.title("🤖 ResuMatch")
st.write("Upload your resume (PDF or image) and paste a job description to get instant feedback.")

# Upload resume
resume_file = st.file_uploader("Upload Resume", type=["pdf", "jpg", "jpeg", "png"])

# Job description input
job_description = st.text_area("Job Description", height=150)

# Analyze button
if st.button("Analyze") and resume_file and job_description:
    file_name = resume_file.name.lower()
    job_description = job_description.strip()

    if file_name.endswith(".pdf"):
        try:
            pdf_bytes = resume_file.read()
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            resume_text = ""
            for page in doc:
                resume_text += page.get_text()
            if not resume_text.strip():
                st.error("Could not extract text from PDF.")
                st.stop()
            data = {
                'resume_text': resume_text,
                'job_description': job_description
            }
            with st.spinner("Analyzing..."):
                response = requests.post(CLOUD_FUNCTION_URL, json=data)
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
            st.stop()

    else:
        mime_type = resume_file.type or 'image/png'
        files = {
            'resume': (resume_file.name, resume_file, mime_type)
        }
        data = {'job_description': job_description}
        with st.spinner("Analyzing..."):
            response = requests.post(CLOUD_FUNCTION_URL, files=files, data=data)

    if response.status_code == 200:
        analysis = response.json().get('analysis')
        if analysis:
            clean_html = markdown.markdown(analysis)
            st.markdown(clean_html, unsafe_allow_html=True)
        else:
            st.warning("No analysis returned.")
    else:
        st.error(f"Error {response.status_code}: {response.text}")
