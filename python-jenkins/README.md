pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'nginx:latest' // Replace with the desired Docker Hub image
    }

    stages {
        stage('Pull Image from Docker Hub') {
            steps {
                script {
                    echo "Pulling Docker image: ${DOCKER_IMAGE}"
                    sh "docker pull ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    echo "Running container using image: ${DOCKER_IMAGE}"
                    sh "docker run -d --name nginx-container -p 8080:80 ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Test Application') {
            steps {
                script {
                    echo "Testing the application running in the container"
                    sh "curl -I http://localhost:8080"
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    echo "Stopping and removing the container"
                    sh "docker stop nginx-container"
                    sh "docker rm nginx-container"
                }
            }
        }
    }
}
