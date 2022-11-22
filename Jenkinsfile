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
                    args '-u root'
                }
            }

            steps {
                sh 'python3 --version'
                sh 'pip --version'
            }
        }

        stage('Dependencies') {
            agent {
                docker {
                    image 'python:latest'
                    // Reuse the same node, avoids having to clone the repository on all nodes
                    reuseNode true
                    args '-u root'
                }
            }

            steps {
                sh 'apt-get update'
                sh 'apt-get install -y libopenmpi-dev'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Tests') {
            parallel {
                stage("PyLint") {
                    agent none
                    stage("PyLint: Dependencies") {
                        agent {
                            docker {
                                image 'python:latest'
                                // Reuse the same node, avoids having to clone the repository on all nodes
                                reuseNode true
                                args '-u root'
                            }
                        }   

                        steps {
                            sh 'pip install pylint'
                        }
                    }
                    stage("PyLint: Test") {
                        agent {
                            docker {
                                image 'python:latest'
                                // Reuse the same node, avoids having to clone the repository on all nodes
                                reuseNode true
                                args '-u root'
                            }
                        }   

                        steps {
                            sh 'python3 -m pylint garlandtools'
                        }
                    }
                }
                stage("PyTest") {
                    agent none
                    stage("PyTest: Dependencies") {
                        agent {
                            docker {
                                image 'python:latest'
                                // Reuse the same node, avoids having to clone the repository on all nodes
                                reuseNode true
                                args '-u root'
                            }
                        }

                        steps {
                            sh 'pip install pytest'
                        }
                    }
                    stage("PyTest: Testing") {
                        agent {
                            docker {
                                image 'python:latest'
                                // Reuse the same node, avoids having to clone the repository on all nodes
                                reuseNode true
                                args '-u root'
                            }
                        }

                        steps {
                            sh 'python3 -m pytest'
                        }
                    }
                }
                stage("Make Distribution") {
                    agent {
                        docker {
                            image 'python:latest'
                            // Reuse the same node, avoids having to clone the repository on all nodes
                            reuseNode true
                            args '-u root'
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
