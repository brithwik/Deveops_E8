=== BMI Calculator Flask App Deployment Steps ===

1. Pre-Requisites:
- Docker Desktop Installed
- Jenkins Installed (Optional for Jenkins build)
- Python (Optional for local testing)

2. Docker Deployment Steps:

cd bmi_calculator_project
docker build -t bmi-calculator-app .
docker run -d -p 5000:5000 bmi-calculator-app

3. Access App:
http://localhost:5000

4. Jenkins Deployment Steps:
- Create Jenkins Pipeline Job
- Use provided Jenkinsfile

App will run inside Docker and be accessible on port 5000.