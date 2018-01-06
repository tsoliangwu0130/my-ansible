pipeline {
  agent {
    node {
      label 'master'
    }
    
  }
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/tsoliangwu0130/my-ansible', branch: 'master')
      }
    }
    stage('Build') {
      steps {
        sh '''for file in $(find . -type f -name "*.yml")
do
	ansible-lint $file
done'''
      }
    }
    stage('Delivery') {
      steps {
        sh '        echo \'Publish artifact over SSH.\''
      }
    }
  }
}