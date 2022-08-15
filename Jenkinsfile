pipeline {
  agent none
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

    stage('Tests') {
      parallel {
        stage('PyLint') {
          agent {
            label 'python3'
          }
          steps {
            sh 'python3 -m pylint garlandtools'
          }
        }

        stage('PyTest') {
          agent {
            label 'python3'
          }
          steps {
            sh 'python3 -m pytest'
          }
        }

        stage('Make distribution package') {
          steps {
            sh 'python3 setup.py sdist'
          }
        }

      }
    }

  }
  options {
    buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '30', numToKeepStr: '3'))
  }
  triggers {
    pollSCM('H/5 * * * *')
  }
}