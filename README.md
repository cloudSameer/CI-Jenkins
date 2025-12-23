# Jenkins CI Pipeline with Python Testing

This project shows how a basic Continuous Integration (CI) pipeline works using Jenkins and GitHub.

The pipeline is created on a local Ubuntu system and automatically runs tests whenever code is updated.

---

## What this project does

When code is pushed to GitHub, Jenkins automatically:

- Pulls the latest code
- Prepares the environment
- Creates a Python virtual environment
- Installs dependencies
- Runs tests using pytest
- Shows test results in Jenkins

If tests fail, the build fails.

---

## Tools used

- Jenkins  
- GitHub  
- Ubuntu Linux  
- Python 3  
- Pytest  

---

## CI pipeline flow

1. Checkout code from GitHub  
2. Install required Python tools  
3. Create and activate a virtual environment  
4. Run automated tests  
5. Publish test results in Jenkins  

---

## Project structure

