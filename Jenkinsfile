pipeline {
    agent none

    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '30', numToKeepStr: '3')
    }

    triggers {
        pollSCM 'H/5 * * * *'
    }

    stages {
        stage('Dependencies') {
            agent {
                label 'python3'
            }

            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install --upgrade -r requirements.txt'
            }
        }

        stage('Run Notebook') {
            agent {
                label 'python3'
            }

            steps {
                sh 'python3 -m nbconvert --execute --inplace  velocities.ipynb'
            }
        }
        stage('Tests') {
            agent none
            parallel {
                stage("PyLint") {
                    agent {
                        label 'python3'
                    }   

                    steps {
                        sh 'pylint garlandtools'
                    }
                }
                stage("PyTest") {
                    agent {
                        label 'python3'
                    }

                    steps {
                        sh 'pytest'
                    }
                }
            }
        }
    }
}
