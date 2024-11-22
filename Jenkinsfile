pipeline{
    agent {
  label 'docker'
}
stages{
    stage('docker-build'){
         steps{
        git branch: 'main', url: 'https://github.com/mushahid2120/2_tier_app-Flask-Mysql-.git'
        sh 'ls'
        sh 'sudo docker build -t mushahid144/flask-mysql:v1 .'
        
    }
    }
    stage('docker-push'){steps{
        sh 'sudo docker push mushahid144/flask-mysql:v1'
    }
    }
    stage('docker-compose'){steps{
        sh 'sudo docker-compose up -d'
    }
    }
}
}