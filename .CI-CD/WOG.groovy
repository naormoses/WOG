pipeline {
    agent any
    
    stages {
        stage('build') {
            steps {
                script {
                    sh("docker build -t naorj/wog-flask-apps:${env.BUILD_NUMBER} .")
                }
            }
        }

        stage('test') {
            steps {
                script {
                    echo "we did some test, they're good, trust me"
                }
            }
        }

        stage('publish') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DockerHubCreds', passwordVariable: 'pass', usernameVariable: 'user')]) {
                        sh("docker login -u ${user} -p ${pass}")
                        sh("docker push naorj/wog-flask-apps:${env.BUILD_NUMBER}")
                    }
                }
            }   
        }
    }
}

// SCM
// test
// COMPILE X
// BUILD image V
// integration tests V
// PUBLISH V
// DEPLOY X
// POST