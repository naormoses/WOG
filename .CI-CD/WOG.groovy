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
                    sh("docker run -d -p 5000:5000 naorj/wog-flask-apps:${env.BUILD_NUMBER}")
                    sh("python3 -m venv venv && source venv/bin/activate && pip3 install selenium")
                    sh("source venv/bin/activate && python3 e2e.py http://host.docker.internal:5000/score")
                }
            }
        }

        stage('publish') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DockerHubCreds', passwordVariable: 'pass', usernameVariable: 'user')]) {
                        sh("docker login -u ${user} -p ${pass}")
                        sh("docker push naorj/wog-flask-app:${env.BUILD_NUMBER}")
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