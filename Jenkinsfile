pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Python Tools') {
            steps {
                sh '''
                sudo dpkg --configure -a || true
                sudo apt-get install -f -y || true
                sudo apt-get update
                sudo apt-get install -y python3-pip python3-venv
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install pytest
                mkdir -p reports
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --junitxml=reports/results.xml
                '''
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}
