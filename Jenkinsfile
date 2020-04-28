node {
        
    
    stage ('run playbook'){
            
            sh 'ansible all -m ping --sudo -u root'
            git 'https://github.com/PramodPolo/clearwater-heat.git'
            sh 'ansible-playbook -v testrc.yaml --sudo -u root'
            
    }
}
