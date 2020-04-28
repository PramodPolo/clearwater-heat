node {
        
    
    stage ('run playbook'){
            
            sh 'ansible all -m ping --sudo -u root"
            sh 'ansible-playbook -v testrc.yaml --sudo -u root'
            
    }
}
