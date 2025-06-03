FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PORT 8080
EXPOSE 8080
CMD ["functions-framework", "--target=analyze_resume", "--port=8080"]