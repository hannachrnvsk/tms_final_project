pipeline {
    agent any
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t test_shop ."
             }
        }
        stage("running tests") {
            steps {
                sh "docker run test_shop pytest -s -v --reruns 3"
            }
        }
    }
}
