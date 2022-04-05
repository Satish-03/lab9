pipeline {
    agent {
        docker {
            image 'node'
            args '-u root'
        }
    } 
    stages {
        stage('Installing/updating packages') {
            steps {
                echo 'Installing/updating packages...'
                sh 'apt-get update'
                sh 'apt-get upgrade -y'
                sh 'apt-get install -y python3-pip'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install ncclient pandas ipaddress netaddr prettytable pylint'
            }
        }
        stage('PEP8 Check') {
            steps {
                echo 'PEP8 Checks...'
                sh 'pylint netman_netconf_obj2.py "--fail-under=5"'
               
                
            }
        }
        stage('Unit tests') {
            steps {
                echo 'Performing unit tests...'
                sh 'python3 -m unittest obj2.py'
            }
        }
    }
}
