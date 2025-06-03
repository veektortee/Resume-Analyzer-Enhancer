import functions_framework
from flask import jsonify, request, Markup
import markdown
from google import genai
from google.cloud import vision
import io
import os

client = genai.Client(vertexai=True, project="phrasal-crowbar-458714-j3", location="us-west1")
chat = client.chats.create(model="gemini-2.0-flash-001")

vision_client = vision.ImageAnnotatorClient()

def extract_text_from_image(file_content):
    image = vision.Image(content=file_content)
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description if texts else ""

@functions_framework.http
def analyze_resume(request):
    try:
        resume_text = ""
        job_description = ""
        
        # Check for multipart/form-data (file upload)
        if request.content_type.startswith("multipart/form-data"):
            resume_file = request.files.get('resume')
            job_description = request.form.get('job_description', '')
            if resume_file:
                content = resume_file.read()
                if resume_file.filename.endswith(('.jpg', '.jpeg', '.png', '.pdf')):
                    resume_text = extract_text_from_image(content)
                else:
                    resume_text = content.decode('utf-8', errors='ignore')
        else:
            # Fallback to JSON payload
            request_json = request.get_json(silent=True)
            resume_text = request_json.get('resume_text', '')
            job_description = request_json.get('job_description', '')

        if not resume_text or not job_description:
            return jsonify({'error': 'Missing resume or job description'}), 400

        prompt = f"""
        Analyze and enhance this resume for the following job:
        Resume: {resume_text}
        Job: {job_description}
        """
        response = chat.send_message(prompt)
        clean_html = markdown.markdown(response.text)
        return jsonify({'analysis': Markup(clean_html)})

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500