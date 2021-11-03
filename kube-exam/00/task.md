##No.1
Deploy a pod named nginx-pod using the nginx:alpine image.
```
kubectl run nginx-pod --image=nginx:alpine --restart=Never
```
##No.2
Deploy a messaging pod using the redis:alpine image with the labels set to tier=msg.

```
kubectl run messaging --generator=run-pod/v1 --restart=Never --image=redis:alpine -l tier=msg
```
##No.3
Create a namespace named apx-x9984574
kubectl create ns apx-x9984574

##No.4
Get the list of nodes in JSON format and store it in a file at /opt/outputs/nodes-z3444kd9.json
```
kubectl get nodes -o json > /opt/outputs/nodes-z3444kd9.json
```
##No.5
Create a service messaging-service to expose the messaging application within the cluster on port 6379

```
kubectl expose pod messaging-application --type=NodePort --port=6379 --name=messaging-application
```

##No.6
Create a deployment named hr-web-app using the image kodekloud/webapp-color with 2 replicas
```
kubectl create deploy hr-web-app --image=kodekloud/webapp-color

kubectl scale deploy hr-web-app --replicas=2
```
##No.7
Create a static pod named static-busybox that uses the busybox image and the command sleep 1000
```
sudo cp static-busybox.yaml /etc/kubernetes/manifests/
sduo systemctl restart kubelet
```
##No.8
Create a static pod named static-busybox that uses the busybox image and the command sleep 1000
```
kubectl run temp-bus -n finance --image=redis:alpine --restart=Never
```
##No.9
A new application orange is deployed. There is something wrong with it. Identify and fix the issue.
```
check:
command sleep
```
##No.10
Expose the hr-web-app as service hr-web-app-service application on port 30082 on the nodes on the cluster
The web application listens on port 8080
```
kubectl expose deployment hr-web-app --type=NodePort --port=8080 --nodePort=30082 --name=hr-web-app-service \
 --dry-run -o yaml > hr-web-app-service.yaml

kubectl -f hr-web-app-service.yaml
```
##No.11 Find node core os
```
kubectl get node -o=jsonpath='{.items[*].status.nodeInfo.osImage}' > /opt/outputs/nodes_os_x43kj56.txt
```
##No.12
Create a Persistent Volume with the given specification.
```
kubectl -f pv.yaml
```
##--END--


