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
                    sudo apt-get update
                    sudo apt-get install -y python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user pytest'
            }
        }
    }
}
