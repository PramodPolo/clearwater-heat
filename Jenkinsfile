node {
    stage ('git clone'){
        git 'https://github.com/PramodPolo/clearwater-heat.git'
    }
    stage ('run playbook'){
               
            sh 'ansible all -m ping --sudo -u root'
            sh 'ansible-playbook -v ansible-playbook.yaml --sudo -u root'
    }
}
