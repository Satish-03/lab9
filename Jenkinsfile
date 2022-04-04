pipeline {
    agent any 
    stages {
        stage('Installing/updating packages') {
            steps {
                echo 'Installing/updating packages...'
                sh 'pip install --upgrade pip'
                sh 'pip3 install ipaddress'
                sh 'pip3 install netaddr'
                sh 'pip3 install prettytable'
                sh 'pip3 install pandas'
                sh 'sudo pip3 install ncclient'
                sh 'sudo pip3 install pylint'
            }
        }
        stage('PEP8 Check') {
            steps {
                echo 'PEP8 Checks...'
                sh 'python3 --version'
               
                
            }
        }
    }
}
