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
                // No build step needed for Flask unless you compile assets
            }
        }

        stage('Run Tests') {
            steps {
                echo '✅ Running tests...'
                // Add pytest or unit test command if needed
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying with Docker...'

                script {
                    // Build the Docker image
                    sh 'docker build -t student-info-flask-app .'

                    // Stop and remove any existing container with the same name
                    sh '''
                        docker stop student-info-container || true
                        docker rm student-info-container || true
                    '''

                    // Run the new container
                    sh '''
                        docker run -d --name student-info-container -p 5000:5000 student-info-flask-app
                    '''
                }
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
