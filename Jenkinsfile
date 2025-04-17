pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/rakshiithaaa/student_information_system_old.git'
            }
        }

        stage('Build Docker Image') {
            steps{
                    // Build the Docker image from the Dockerfile located in the root directory
                    sh 'docker build -t flask-app .'
            }
        }

        stage('Run Flask Container'){
            steps{
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
}
