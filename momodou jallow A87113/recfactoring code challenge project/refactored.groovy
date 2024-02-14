// Improved Jenkinsfile for CI/CD pipeline

def buildCommand = 'make'
def testCommand = 'make test'
def deployCommand = 'make deploy'

pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                executeCommand(buildCommand, 'Building')
            }
        }
        
        stage('Test') {
            steps {
                executeCommand(testCommand, 'Testing')
            }
        }
        
        stage('Deploy') {
            steps {
                executeCommand(deployCommand, 'Deploying')
            }
        }
        
        // Other stages...
    }
}

def executeCommand(String command, String action) {
    try {
        sh command
    } catch (Exception e) {
        echo "${action} failed: ${e.message}"
        currentBuild.result = 'FAILURE'
        error "Failed to ${action}"
    }
}
