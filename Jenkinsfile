node {
    stage ('git clone'){
        git 'https://github.com/PramodPolo/clearwater-heat.git'
    }
    
    
    
    stage ('Approve'){
            input 'review git and approve'
               
           }
    stage ('run playbook'){
            sh 'ansible all -m ping --sudo -u root'
            sh 'ansible-playbook -v adminrc.sh --sudo -u root'
    }
}
