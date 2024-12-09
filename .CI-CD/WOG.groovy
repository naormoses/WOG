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

        stage('scan image') {
            steps {
                script {
                    sh("docker images")
                }
            }
        }

        stage('test') {
            steps {
                script {
                    sh("docker run -d -p 5000:5000 wog-flask-app:${env.BUILD_NUMBER}")
                    sh("pip3 install selenium && python3 e2e.py http://host.docker.internal:5000/score")
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

    // post {
    //     always {}
    //     success{}
    //     failure{}
    //     unstable{}
    // }
}