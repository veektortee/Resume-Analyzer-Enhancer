# Use the official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Cloud Run uses
ENV PORT 8080
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]