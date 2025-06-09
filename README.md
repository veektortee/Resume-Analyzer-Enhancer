# ResuMatch: Resume Enhancement Application

ResuMatch is a cloud-native application designed to analyze and enhance resumes based on specific job descriptions. It integrates AI-powered content analysis with a user-friendly web interface.

## 🌟 Features
- Analyze resumes in PDF or image formats.
- Tailor analysis to specific job descriptions.
- Clean and structured HTML rendering with markdown support.
- Seamless file upload and user interaction.
- Deployed entirely on Cloud Run with a Flask backend and frontend.

## 📹 Demo Video
Watch the full demo [here](https://www.youtube.com/watch?v=o00hYlLGNeI).

### 🎯 Try the App Now
✅ Test the **Streamlit version** of ResuMatch here:  
👉 [https://resumatch.streamlit.app](https://resume-analyzer-enhancer-dt5hzqb6rsvwczcfcy3ppz.streamlit.app/)

> Upload your resume, paste a job description, and get instant AI-powered feedback.

## 🚀 Technologies
- **Google Cloud Platform**: Vertex AI (Gemini), Cloud Run, IAM.
- **Python Flask**: Backend API + web UI (Cloud Run).
- **Streamlit**: Interactive frontend for quick testing and public access.
- **Markdown + Markupsafe**: For clean HTML rendering.
- **Docker**: Containerized deployment for frontend and backend.

## 📁 Project Structure
```
resumatch/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py # Flask app
│   ├── requirements.txt
│   └── Dockerfile
├── streamlit_app/
│ ├── app.py # Streamlit app
│   └── requirements.txt
└── README.md
```

## 📦 Deployment
### Backend Deployment
1. Build and submit the backend Docker image:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/resumatch-backend
   ```
2. Deploy the backend to Cloud Run:
   ```bash
   gcloud run deploy resumatch-backend --image gcr.io/YOUR_PROJECT_ID/resumatch-backend --platform managed --region YOUR_REGION --allow-unauthenticated
   ```

### Frontend Deployment (Flask on Cloud Run)
1. Build and submit the frontend Docker image:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/resumatch-frontend
   ```
2. Deploy the frontend to Cloud Run:
   ```bash
   gcloud run deploy resumatch-frontend --image gcr.io/YOUR_PROJECT_ID/resumatch-frontend --platform managed --region YOUR_REGION --allow-unauthenticated
   ```
### Frontend Deployment (Flask on Cloud Run)
1. Push streamlit_app/app.py and requirements.txt to a public GitHub repo.
2. Go to https://share.streamlit.io.
3. Connect your repo and deploy
   
## 💡 Future Enhancements
- Support for additional languages and resume formats.
- Enhanced UI design with animations and interactivity.

## 🔒 Security Considerations
- Scoped IAM roles for secure API access.
- Secrets and service account keys are excluded from version control.
