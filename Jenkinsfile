node {
    stage ('git clone'){
        git 'https://github.com/PramodPolo/clearwater-heat.git'
    }
    stage ('run playbook'){
        
        stage ('SonarQube analysis') 
           withSonarQubeEnv('sonarcube') {
           // requires SonarQube Scanner for Maven 3.2+
           sh 'mvn org.sonarsource.scanner.maven:sonar-maven-plugin:3.2:sonar'

            stage 'Approve'
            input 'review sonar results and approve'

               
            sh 'ansible all -m ping --sudo -u root'
            sh 'ansible-playbook -v ansible_playbook.yaml --sudo -u root'
    }
}
