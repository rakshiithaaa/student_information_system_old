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
        // stop & remove any old container on 5000 to avoid port conflicts
        sh '''
          docker rm -f flask-app || true
          docker run -d --name flask-app -p 5000:5000 flask-app
        '''
      }
    }
  }

  post {
    always {
      echo "Cleaning up dangling images..."
      sh 'docker image prune -f'
    }
  }
}
