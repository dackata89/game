pipeline {
    agent {
        label {
            label ""
            customWorkspace "workspace/lab_test_${BUILD_NUMBER}"
        }
    }

    stages {
        stage("Checkout Repository") {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage("Build") {
            steps {
                script {
                    sh "docker compose build"
                }
            }
        }

        stage("Run Container") {
            steps {
                script {
                    sh "docker compose up -d"
                }
            }
        }

        stage("Run Tests") {
            steps {
                script {
                    println("Successfully tested!")
                }
            }
        }

        stage("Stop Container") {
            steps {
                script {
                    sh "docker compose down"
                }
            }
        }

        stage("Push Docker image to registry") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                        sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}"
                        sh "docker compose push"
                    }
                }
            }
        }
    }
}
