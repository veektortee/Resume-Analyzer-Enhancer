import streamlit as st
import requests
import markdown
from markupsafe import Markup

CLOUD_FUNCTION_URL = 'https://resumatch-backend-790682135616.us-west1.run.app'

st.title("🤖 ResuMatch")
st.write("Upload your resume (PDF or image) and paste a job description to get instant feedback.")

# Upload resume
resume_file = st.file_uploader("Upload Resume", type=["pdf", "jpg", "jpeg", "png", "txt"])

# Job description input
job_description = st.text_area("Job Description", height=150)

# Analyze button
if st.button("Analyze") and resume_file and job_description:
    files = {
        'resume': (resume_file.name, resume_file, resume_file.type)
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
