# Getting started with k8s local cluster

## Requirements
* minikube
* kubectl
* docker

## Installing `minikube`

Installation guide is [here](https://minikube.sigs.k8s.io/docs/start/).

### MacOS
```shell
brew install minikube
```

## Installing `kubectl`

Detailed installation guide [here](https://kubernetes.io/docs/tasks/tools/).

### MacOS
```shell
brew install kubectl
```

## Install `docker`
Install docker for your OS from [here](https://docs.docker.com/get-docker/).
``
## Getting started

### Start local k8s cluster
```shell
minikube start --memory 10000 --cpus 4 \
--driver=docker --kubernetes-version=v1.21.6 \
--mount
```

### Check the installation
Open kubernetes dashboard:
```shell
minikube dashboard
```

### Build Docker image
#### locally
```shell
cd docker
docker build -t demo_image .
minikube image load demo_image
```

#### inside minikube (faster)
* SSH into minikube
```shell
minikube ssh
```

* Build your docker image
```shell
cd /minikube-host/<USER>/Repos/data-max/workshop-epoka/docker
docker build -t demo_image .
```

### Install the application (outside of minikube)
```shell
cd ../kubernetes
kubectl apply -f deployment.yaml
```

### Make application reachable
```shell
kubectl port-forward svc/flask-service 5000:5000
```
At `localhost:5000` you should see the hello message.

### Send request

```shell
curl --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
"fixed acidity": 5,
"volatile acidity": 5,
"citric acid":5,
"residual sugar": 5,
"chlorides": 5,
"free sulfur dioxide": 5,
"total sulfur dioxide": 5,
"density": 5,
"pH": 5,
"sulphates": 5,
"alcohol": 5
}'
```

### Change replica count
Change line 23 in `deployment.yaml`.
```shell
kubectl apply -f deployment.yaml
```

### Clean up
```shell
minikube delete
```

### References
https://github.com/noahgift/kubernetes-hello-world-python-flask