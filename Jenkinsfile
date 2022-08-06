properties([pipelineTriggers([pollSCM('* * * * * ')])])
node {
    stage("clone") {
        git "https://github.com/omerk14/SummaryProject.git"
    }
    stage("show files"){
        bat "dir"
    }
    stage("Build and start test image") {
        steps {
                sh "docker-composer build"
                sh "docker-compose up -d"

            }
        }
    stage("Run the image") {
    sh """
                    sudo docker run --name summary -d summary:latest
                """
    }
}