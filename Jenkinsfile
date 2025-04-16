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
            steps {
                script {
                    // Build the Docker image from the Dockerfile located in the root directory
                    sh 'docker build -t flask-app .'
                }
            }
        }

        stage('Run Flask App in Docker') {
            steps {
                script {
                    // Run the Flask app in a container
                    sh 'docker run -d -p 5000:5000 flask-app'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying the application...'
                // Add deployment steps here (e.g., pushing to production server)
            }
        }
    }

    post {
        always {
            script {
                currentBuild.result = 'SUCCESS'
            }
        }
    }
}
