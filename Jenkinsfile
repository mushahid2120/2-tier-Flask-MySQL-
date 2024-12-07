pipeline{
    agent none
stages{
    stage('docker-build'){
        agent { label 'docker' }
        steps{
        git branch: 'main', url: 'https://github.com/mushahid2120/2_tier_app-Flask-Mysql-.git'
        sh 'ls'
        sh 'sudo docker build --rm -t mushahid144/flask-mysql:v1 . '
        sh 'sudo docker push mushahid144/flask-mysql:v1'
    }
    }
    stage('docker-compose'){
        agent { label 'k8s' }
        steps{
        git branch: 'main', url: 'https://github.com/mushahid2120/2_tier_app-Flask-Mysql-.git'
        dir("kubernetes") {
                        sh 'sudo kubectl apply -f pv-pvc-mysql.yaml'
                        sh 'sudo kubectl apply -f configmap.yaml'
                        sh 'sudo kubectl apply -f secret.yaml'
                        sh 'sudo kubectl apply -f deploy-mysql.yaml'
                        sh 'sudo kubectl apply -f svc-mysql.yaml'
                        sh 'sudo kubectl apply -f svc-flask.yaml'
                        sh 'sudo kubectl apply -f deploy-flask.yaml'
                        sh 'sleep 20s'
                        sh 'sudo kubectl get all'
                    }
    }
    }
}
}
