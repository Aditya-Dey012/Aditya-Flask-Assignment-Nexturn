pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = 'aditya2002dey'  //  Docker Hub username
        DOCKER_IMAGE = 'flask-api'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Aditya-Dey012/Aditya-Flask-Assignment-Nexturn.git'  //git  repo
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh "docker tag ${DOCKER_IMAGE} ${DOCKER_HUB_USER}/${DOCKER_IMAGE}"
                sh "docker push ${DOCKER_HUB_USER}/${DOCKER_IMAGE}"
            }
        }
        stage('Deploy Container') {
            steps {
                sh "docker run -d -p 5000:5000 ${DOCKER_HUB_USER}/${DOCKER_IMAGE}"
            }
        }
    }
}
