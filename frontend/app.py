# frontend/app.py
from flask import Flask, request, render_template
app = Flask(__name__)

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
    # For now, save locally
    resume.save(f"./data/{resume.filename}")
    return f"Received {resume.filename} and job description"

if __name__ == '__main__':
    app.run(debug=True)