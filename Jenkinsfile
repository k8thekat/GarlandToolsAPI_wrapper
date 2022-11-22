pipeline {
    agent {
        label 'docker'
    }

    stages {
        stage('Versions') {
            agent {
                docker {
                    image 'python:latest'
                    // Reuse the same node, avoids having to clone the repository on all nodes
                    reuseNode true
                }
            }

            steps {
                sh 'python3 --version'
                sh 'python3 -m pip --version'
            }
        }

        stage('Dependencies') {
            agent {
                docker {
                    image 'python:latest'
                    // Reuse the same node, avoids having to clone the repository on all nodes
                    reuseNode true
                }
            }

            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Tests') {
            parallel {
                stage("PyLint") {
                    agent {
                        docker {
                            image 'python:latest'
                            // Reuse the same node, avoids having to clone the repository on all nodes
                            reuseNode true
                        }
                    }   

                    steps {
                        sh 'python3 -m pylint garlandtools'
                    }
                }
                stage("PyTest") {
                    agent {
                        docker {
                            image 'python:latest'
                            // Reuse the same node, avoids having to clone the repository on all nodes
                            reuseNode true
                        }
                    }

                    steps {
                        sh 'python3 -m pytest'
                    }
                }
                stage("Make Distribution") {
                    agent {
                        docker {
                            image 'python:latest'
                            // Reuse the same node, avoids having to clone the repository on all nodes
                            reuseNode true
                        }
                    }

                    steps {
                        sh 'python3 setup.py sdist'
                    }
                }
            }
        }
    }
}
