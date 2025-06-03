from flask import Flask, request, render_template_string
from markupsafe import Markup
import requests
import markdown

app = Flask(__name__)
CLOUD_FUNCTION_URL = 'https://resumatch-backend-790682135616.us-west1.run.app'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>ResuMatch</title></head>
<body>
<h2>Welcome to ResuMatch!</h2>
<p>Upload your resume (PDF or image) and job description to get instant feedback.</p>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="resume" accept=".pdf,.jpg,.jpeg,.png,.txt"/><br>
<textarea name="job_description" rows="5" cols="50" placeholder="Paste the job description here"></textarea><br>
<input type="submit" value="Analyze">
</form>
{% if analysis %}
<h3>Analysis Result:</h3><div>{{ analysis|safe }}</div>
{% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    analysis = None
    if request.method == 'POST':
        resume_file = request.files.get('resume')
        job_description = request.form.get('job_description')
        files = {'resume': (resume_file.filename, resume_file.stream, resume_file.mimetype)} if resume_file else None
        data = {'job_description': job_description}
        response = requests.post(CLOUD_FUNCTION_URL, files=files, data=data)
        if response.status_code == 200:
            analysis = response.json().get('analysis')
            if analysis:
                clean_html = markdown.markdown(analysis)
                analysis = Markup(clean_html)
        else:
            analysis = f"Error {response.status_code}: {response.text}"

    return render_template_string(HTML_TEMPLATE, analysis=analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)