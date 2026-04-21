pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')   // check every 1 min
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/itsChandramahesh/sugar_test_predictor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp1 .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop myapp || true'
                sh 'docker rm myapp || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name myapp1 myapp1'
            }
        }
    }
}