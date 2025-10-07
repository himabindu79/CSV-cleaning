pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 -m pip install --user pandas
                '''
            }
        }
        
        stage('Clean CSV Files') {
            steps {
                echo 'Cleaning CSV files...'
                sh 'python3 clean_csv.py'
            }
        }
        
        stage('Commit Cleaned Files') {
            steps {
                echo 'Committing cleaned files back to repo...'
                sh '''
                    git config user.email "jenkins@yourdomain.com"
                    git config user.name "Jenkins CI"
                    git add cleaned_data/
                    git diff --staged --quiet || git commit -m "Auto-cleaned CSV files [skip ci]"
                    git push origin ${GIT_BRANCH}
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}