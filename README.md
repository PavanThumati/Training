# jenkins-Training
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/DevOlabodeM/pytest-intro-vs-M']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/DevOlabodeM/pytest-intro-vs-M'
                sh 'python3 ops.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}
