pipeline {
    agent {
        label 'docker'
    }

    stages {
        stage('Versions') {
            agent {
                docker {
                    image 'python3:latest'
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
                    image 'python3:latest'
                    // Reuse the same node, avoids having to clone the repository on all nodes
                    reuseNode true
                }
            }

            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install --upgrade -r requirements.txt'
            }
        }

        stage('Tests') {
            parallel {
                stage("PyLint") {
                    agent {
                        docker {
                            image 'python3:latest'
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
                            image 'python3:latest'
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
                            image 'python3:latest'
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
