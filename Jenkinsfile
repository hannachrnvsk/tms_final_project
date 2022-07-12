pipeline {
    agent {
        label 'master'
        }
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t test_shop ."
                sh "docker run test_shop pytest -s -v --reruns 3"
            }
        }
    }
}