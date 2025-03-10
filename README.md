docker swarm join --token SWMTKN-1-26ne2b6iniz5stpfp59dbha7idzg5whjjtcqiva6v6u5o8i0ap-2bsgt2j19khln8q45tpc24py2 192.168.219.134:2377


# jenkins-Training
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/PavanThumati/pytest-intro-vs-M-jenkins.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/PavanThumati/pytest-intro-vs-M-jenkins.git'
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
