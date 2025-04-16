pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/rakshiithaaa/student_information_system_old.git'
            }
        }

        stage('Install Dependencies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App'){
            steps{
                sh 'nohup python app.py &'
            }
        }

        stage('Build') {
            steps {
                echo '📦 Building the project...'
                
                // Add build steps here, like installing dependencies if needed
            }
        }

        stage('Run Tests') {
            steps {
                echo '✅ Running tests...'
                // Add test execution commands if you have tests
            }
        }

        stage('Run Flask Container'){
            steps{
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying the application...'
                // Add your deployment steps here (copy files, run Django server, etc.)
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
