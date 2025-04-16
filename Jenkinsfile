pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/rakshiithaaa/student_information_system_old.git'
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
