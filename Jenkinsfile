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
        // ensure we pick up your updated Dockerfile & requirements.txt
        sh 'docker build --no-cache -t flask-app .'
      }
    }

    stage('Run Flask Container') {
      steps {
        // Stop any container using port 5000, remove old flask-app, then run fresh
        sh '''
          echo "🧼 Cleaning up any container using port 5000..."
          PORT_CONTAINER=$(docker ps -q --filter "publish=5000")
          if [ -n "$PORT_CONTAINER" ]; then
            docker stop $PORT_CONTAINER
            docker rm $PORT_CONTAINER
          fi

          echo "🛑 Removing existing flask-app container (if any)..."
          docker rm -f flask-app || true

          echo "🚀 Starting new flask-app container on port 5000..."
          docker run -d --name flask-app -p 5000:5000 flask-app
        '''
      }
    }
  }

  post {
    always {
      echo "🧹 Cleaning up dangling Docker images..."
      sh 'docker image prune -f'
    }
  }
}
