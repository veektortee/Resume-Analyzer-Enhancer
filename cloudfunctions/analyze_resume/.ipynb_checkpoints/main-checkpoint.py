# cloudfunctions/analyze_resume/main.py
import functions_framework

@functions_framework.http
def analyze_resume(request):
    request_json = request.get_json()
    resume_text = request_json.get('resume_text')
    job_description = request_json.get('job_description')
    # Placeholder response
    return {'message': f"Resume and Job Description received. Processing..."}