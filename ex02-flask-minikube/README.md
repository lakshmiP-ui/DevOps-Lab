# Exercise 2 - Deploy a Flask app on Minikube

## Aim
Deploy a Flask app on Minikube using kubectl and YAML.

## Steps and output
1. Started Minikube: `minikube start`
   ![status](images/01-minikube-status.png)
2. Built the image: `docker build -t flask-app .`
3. Deployed: `kubectl apply -f flask-deployment.yaml`
   ![pods](images/03-pods.png)
...

## Result
![Flask working](images/06-flask-working.png)
