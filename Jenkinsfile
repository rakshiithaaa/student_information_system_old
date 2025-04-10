pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Step 1: Checkout code from GitHub
                git branch: 'main', url: 'https://github.com/rakshiithaaa/student_information_system.git'
            }
        }
        

        stage('Build Docker Image') {
            steps {
                // Step 2: Build the Docker image
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // Step 3: Stop and remove any existing container
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'

                // Step 4: Run the Docker container
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }
    }

    post {
        always {
            // Step 5: Notify that the pipeline is complete
            echo 'Pipeline execution completed.'
        }
    }
}
