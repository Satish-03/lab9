pipeline {
    agent docker 
    stages {
        stage('PEP8 Check') {
            steps {
                echo 'PEP8 Checks...'
                sh 'python3 --version'
                echo 'Hi Satish, you made it'
                echo 'Email sent'
                sh 'pylint /home/netman/NetMan/lab9/lab-9-Satish-03-main/netman_netconf_obj2.py "--fail-under=5"'
               
                
            }
        }
    }
}
