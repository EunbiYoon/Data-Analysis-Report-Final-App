#!/bin/bash

yum update -y
amazon-linux-extras install epel -y
yum install nginx -y
yum install git -y
yum install gcc -y
yum install build-essential -y
yum install python3-pip python3-devel python3-setuptools -y

git config --system credential.https://git-codecommit.us-east-2.amazonaws.com.helper '!aws --profile default codecommit credential-helper $@'
git config --system credential.https://git-codecommit.us-east-2.amazonaws.com.UseHttpPath true

aws configure set region us-east-2

mkdir -p /var/www

git clone https://git-codecommit.us-east-2.amazonaws.com/v1/repos/flasktodo /var/www

cd /var/www

git config core.fileMode false

aws s3 cp s3://tci-s3-demo3/flask-todo/.env .env

chmod +x scripts/post_userdata.sh

./scripts/post_userdata.sh