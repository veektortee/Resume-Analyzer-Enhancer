from flask import Flask, request, render_template
import requests

app = Flask(__name__)

CLOUD_FUNCTION_URL = 'YOUR_CLOUD_FUNCTION_URL_HERE'  # Replace with actual deployed URL

@app.route('/')
def upload_form():
    return '''
        <form method="POST" enctype="multipart/form-data" action="/upload">
            <input type="file" name="resume">
            <textarea name="job_description" placeholder="Paste job description"></textarea>
            <input type="submit" value="Analyze">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    resume = request.files['resume']
    job_description = request.form['job_description']
    
    # Read resume text (for now, we’ll just read it as string)
    resume_text = resume.read().decode('utf-8', errors='ignore')
    
    # Prepare payload
    payload = {
        'resume_text': resume_text,
        'job_description': job_description
    }
    
    # Call the Cloud Function
    response = requests.post(CLOUD_FUNCTION_URL, json=payload)
    
    return f"Response from Cloud Function: {response.json()}"

if __name__ == '__main__':
    app.run(debug=True)