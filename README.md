# ResuMatch: Resume Enhancement Application

ResuMatch is a cloud-native application designed to analyze and enhance resumes based on specific job descriptions. It integrates AI-powered content analysis with a user-friendly web interface.

## 🌟 Features
- Analyze resumes in PDF or image formats.
- Tailor analysis to specific job descriptions.
- Clean and structured HTML rendering with markdown support.
- Seamless file upload and user interaction.
- Deployed entirely on Cloud Run with a Flask backend and frontend.

## 📹 Demo Video
Watch the full demo [here](https://www.youtube.com/watch?v=o00hYlLGNeI)

## 🚀 Technologies
- Google Cloud Platform: Vertex AI (Gemini models), Cloud Run, IAM.
- Python Flask for both backend and frontend services.
- Markdown and Markupsafe for safe HTML rendering.
- Docker for containerized deployment.

## 📁 Project Structure
```
resumatch/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
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

### Frontend Deployment
1. Build and submit the frontend Docker image:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/resumatch-frontend
   ```
2. Deploy the frontend to Cloud Run:
   ```bash
   gcloud run deploy resumatch-frontend --image gcr.io/YOUR_PROJECT_ID/resumatch-frontend --platform managed --region YOUR_REGION --allow-unauthenticated
   ```

## 💡 Future Enhancements
- Support for additional languages and resume formats.
- Enhanced UI design with animations and interactivity.

## 🔒 Security Considerations
- Scoped IAM roles for secure API access.
- Secrets and service account keys are excluded from version control.
