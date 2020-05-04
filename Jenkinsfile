node {
    stage ('git clone'){
        git 'https://github.com/PramodPolo/clearwater-heat.git'
    }
    stage('Sonarqube') {
    environment {
        scannerHome = tool 'SonarQubeScanner'
    }
    steps {
        withSonarQubeEnv('sonarqube') {
            sh "${scannerHome}/bin/sonar-scanner"
        }
        timeout(time: 10, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
        }
    }
}
    
    
    stage ('Approve'){
            input 'review git and approve'
               
           }
    stage ('run playbook'){
            sh 'ansible all -m ping --sudo -u root'
            sh 'ansible-playbook -v adminrc.sh --sudo -u root'
    }
}
