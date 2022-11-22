pipeline {
    agent {
        label 'docker'
    }

    stages {
        stage("PyLint") {
            agent {
                docker {
                    image 'python:latest'
                    args '-u root'
                }
            }   

            steps {
                sh 'apt-get update'
                sh 'apt-get install -y libopenmpi-dev'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'pip install pylint'
                sh 'pylint garlandtools'
            }
        }

        stage("PyTest: Testing") {
            agent {
                docker {
                    image 'python:latest'
                    args '-u root'
                }
            }

            steps {
                sh 'apt-get update'
                sh 'apt-get install -y libopenmpi-dev'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
                sh 'pytest'
            }
        }

        stage("Make Distribution") {
            agent {
                docker {
                    image 'python:latest'
                    args '-u root'
                }
            }

            steps {
                sh 'apt-get update'
                sh 'apt-get install -y libopenmpi-dev'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'python3 setup.py sdist'
            }
        }
    }
}
