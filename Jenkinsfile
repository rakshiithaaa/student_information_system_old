pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/rakshiithaaa/student_information_system_old.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '📦 Building Docker image...'
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Flask Container') {
            steps {
                echo '🚀 Running Flask container...'
                sh 'docker run -d -p 5000:5000 --name flask-app-container flask-app'
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline finished with status: ${currentBuild.currentResult}"
        }
    }
}
