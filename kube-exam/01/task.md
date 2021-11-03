##No.1
Take a backup of the etcd cluster and save it to /tmp/etcd-backup.db

check version
```
ETCDCTL_API=3 etcdctl --version
```
check connection
```
ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key=/etc/kubernets/pki/etcd/healthcheck-client.key member list
```
save
```
ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key=/etc/kubernetes/pki/etcd/healthcheck-client.key snapshot save /tmp/etcd-backup.db
```
verify the status
```
ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key=/etc/kubernets/pki/etcd/healthcheck-client.key snapshot status /tmp/etcd-backup.db -w table
```

##No.2
Create a Pod called redis-storage with image: redis:alpine with a Volume of type emptyDir that lasts for the life of the Pod. Specs on the right.
Pod named 'redis-storage' created
Pod 'redis-storage' uses Volume type of emptyDir
Pod 'redis-storage' uses volumeMount with mountPath = /data/redis
```
kubectl run redis-storage --image=redis:alpine --restart=Never -o yaml --dry-run > redis-storage.yaml

kubectl apply -f redis-torage.yaml
```

##No.3
Create a new pod called super-user-pod with image busybox:1.28. Allow the pod to be able to set system_time
The container should sleep for 4800 seconds
Pod: super-user-pod
Container Image: busybox:1.28
SYS_TIME capabilities for the conatiner?

```
kubectl apply -f redis-torage.yaml
```

##No.4
A pod definition file is created at /root/use-pv.yaml. Make use of this manifest file and mount the persistent volume called pv-1. Ensure the pod is running and the PV is bound.
mountPath: /data persistentVolumeClaim Name: my-pvc
persistentVolume Claim configured correctly
pod using the correct mountPath
pod using the persistent volume claim?
```
kubectl apply -f pvc.yaml
kubectl get pv
```
##No.5

Create a new deployment called nginx-deploy, with image nginx:1.16 and 1 replica. Record the version. Next upgrade the deployment to version 1.17 using rolling update. Make sure that the version upgrade is recorded in the resource annotation.
Deployment : nginx-deploy. Image: nginx:1.16
Image: nginx:1.16
Task: Upgrade the version of the deployment to 1:17
Task: Record the changes for the image upgrade
```
kubectl run nginx-deploy --image=nginx:1.16 --replicas=1 --record
kubectl rollout history deploy nginx-deploy
kubectl set image deployment/nginx-deploy nginx-deploy=nginx:1.17 --record
```
verify
```
kubectl rollout history deploy nginx-deploy
kubectl describe deploy nginx-deploy | grep -i image | awk '{$1}' | xargs kubectl describe pod  | grep image
```

##No.6
Create a new user called john. Grant him access to the cluster. John should have permission to create, list, get, \
update and delete pods in the development namespace . The private key exists in the location: /root/john.key and csr at /root/john.csr
CSR: john-developer Status:Approved
Role Name: developer, namespace: development, Resource: Pods
Access: User 'john' has appropriate permissions
```
openssl genrsa -out john.key 2048
openssl req -new -key john.key -out john.csr

cat john.csr | base64 | tr -d "n"

cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: john-developer
spec:
  request: {put result from command above here!}
  usages:
    - digital signature
    - key encipherment
    - server auth
EOF

kubectl get csr

kubectl certificate approve john-developer
kubectl get csr
```
Create role developer
```
kubectl create role developer --resource=pods --verb=create,list,get,update,delete --namespace=development
```
Verify
```
kubectl describe role developer -n development
```
Create rolebinding
```
kubectl create rolebinding developer-role-binding --role=developer --user=john  --namespace=development
```
Verify
```
kubectl describe rolebinding.rbac.authorization.k8s.io developer-role-binding -n development
kubectl auth can-i update pods --namespace=development --as=john
kubectl auth can-i create pods --namespace=development --as=john
kubectl auth can-i list pods --namespace=development --as=john
kubectl auth can-i get pods --namespace=development --as=john
kubectl auth can-i delete pods --namespace=development --as=john
```

##No.7
Create an nginx pod called nginx-resolver using image nginx, expose it internally with a service called nginx-resolver-service. Test that you are able to look up the service and pod names from within the cluster. Use the image: busybox:1.28 for dns lookup. Record results in /root/nginx.svc and /root/nginx.pod
Pod: nginx-resolver created
Service DNS Resolution recorded correctly
Pod DNS resolution recorded correctly
```
kubectl run nginx-resolver --image=nginx --generator=run-pod/v1
```
Create service
```
kubectl expose pod nginx-resolver --name=nginx-resolver-service  --port=80 --target-port=80 --type=ClusterIP
```
verify svc
```
kubectl describe svc nginx-resolver-service
kubectl get pod nginx-resolver -o wide
```
nslookup
It doesn't work,I think the image is not good.
```
kubectl run --generator=run-pod/v1 test-nslookup --image=busybox:1.28 --rm -it -- nslookup nginx-resolver-service
```
method1 :copy the result for the logs,without server
```
kubectl logs test-nslookup
```
method2 : didn't work
```
kubectl run --generator=run-pod/v1 test-nslookup --image=busybox:1.28 --rm -it -- nslookup nginx-resolver-service > /root/nginx.svc
```
##No.8
Create a static pod on node01 called nginx-critical with image nginx. Create this pod on node01 and make sure that it is recreated/restarted automatically in case of a failure.
Use /etc/kubernetes/manifests as the Static Pod path for example.
Kubelet Configured for Static Pods
Pod nginx-critical-node01 is Up and running

ssh node01

Check configure --config's path
```
systemctl status kubelet
```
Get the static pod's path
```
cd /var/lib/kubelet/
cat config.yaml | grep static
```
Get the path is /etc/kubernetes/manifests
```
cd /etc/kubernetes/
```
Create directory manifests
```
mkdir manifests
```
Back to master
```
kubectl run --generator=run-pod/v1 nginx-critical --image=nginx --dry-run -o yaml > nginx-critical.yaml

cat nginx-critical.yaml
```
Login to node01
```
ssh node01

docker ps | grep -i nginx
```
create static in /etc/kubernetes/manifests
```
cd /etc/kubernetes/manifests

cat <<EOF | tee nginx-critical.yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: nginx-critical
    name: nginx-critical
spec:
  containers:
  - image: nginx
    name: nginx-critical
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
EOF
