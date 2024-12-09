pipline {
    agent any
    
    stages {
        stage('test') {
            steps {
                script {
                    sh("docker ps")
                }
            }
        }
    }
}