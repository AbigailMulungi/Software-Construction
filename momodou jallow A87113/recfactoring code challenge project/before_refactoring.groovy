// Example Jenkinsfile for CI/CD pipeline
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Build steps
                sh 'make'
            }
        }
        
        stage('Test') {
            steps {
                // Test steps
                sh 'make test'
            }
        }
        
        stage('Deploy') {
            steps {
                // Deployment steps
                sh 'make deploy'
            }
        }
        
        // Other stages...
    }
}
