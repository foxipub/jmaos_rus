##No.1
Create a new service account with the name pvviewer. Grant this Service account access to list all PersistentVolumes in the cluster by creating an appropriate cluster role called pvviewer-role and ClusterRoleBinding called pvviewer-role-binding.
Next, create a pod called pvviewer with the image: redis and serviceAccount: pvviewer in the default namespace
ServiceAccount: pvviewer
ClusterRole: pvviewer-role
ClusterRoleBinding: pvviewer-role-binding
Pod: pvviewer
Pod configured to use ServiceAccount pvviewer ?

Create sa
```
kubectl create sa pvviewer
```
Create clusterrole
```
kubectl create clusterrole  pvviewer-role --resource=persistentvolumes  --verb=list
```
Create cluster role binding
```
kubectl create clusterrolebinding pvviewer-role-binding --clusterrole=pvviewer-role --serviceaccount=default:pvviewer
```
##No.2
List the InternalIP of all nodes of the cluster. Save the result to a file /root/node_ips
Answer should be in the format: InternalIP of master<space>InternalIP of node1<space>InternalIP of node2<space>InternalIP of node3 (in a single line)
Get ExternalIPs of all nodes

Check get internalip
```
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'
```
copy the stuff to node_ips file
```
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}' > /root/node_ips
```
Verify the node_ips file
```
cat /root/node_ips
```
##No.3
Create a pod called multi-pod with two containers. \
Container 1, name: alpha, image: nginx \
Container 2: beta, image: busybox, command sleep 4800 \
Environment Variables: \
container 1: \
name: alpha \
Container 2: \
name: beta \
Pod Name: multi-pod \
Container 1: alpha \
Container 2: beta \
Container beta commands set correctly? \
Container 1 Environment Value Set \
Container 2 Environment Value Set \
```
kubectl run --generator=run-pod/v1 alpha --image=nginx --dry-run -o yaml > multi-pod.yaml
```
check
```
kubectl describe pod multi-pod
```
or
```
kubectl exec -it multi-pod -- sh
printenv
```
##No.4
Create a Pod called non-root-pod , image: redis:alpine \
runAsUser: 1000 \
fsGroup: 2000 \

kubectl run non-root-pod --generator=run-pod/v1 --image=redis:alpine --dry-run -o yaml > non-root-pod.yaml

##No.5
We have deployed a new pod called np-test-1 and a service called np-test-service. \
Incoming connections to this service are not working. Troubleshoot and fix it.
Create NetworkPolicy, by the name ingress-to-nptest that allows incoming connections to the service over port 80.
```
kubectl run --generator=run-pod/v1 test-np --image=busybox:1.28 --rm -it -- sh
nc -z -v -w 2 np-test-service 80
```
Check network policy
```
kubectl describe netpol defautl-deny
```
Create network policy
https://kubernetes.io/docs/concepts/services-networking/network-policies/#the-networkpolicy-resource

```
kubectl apply -f network-policy.yaml
```
Check network version
```
kubectl api-versions | grep -i network
```
Check again
```
kubectl run --generator=run-pod/v1 test-np --image=busybox:1.28 --rm -it -- sh
nc -z -v -w 2 np-test-service 80
```
##No.6
Taint the worker node node01 to be Unschedulable. Once done, create a pod called dev-redis, image redis:alpine to ensure workloads \
are not scheduled to this worker node. Finally, create a new pod called prod-redis and image redis:alpine with \
toleration to be scheduled on node01. \
Key = env_type \
Value = production \
Effect = NoSchedule \
pod 'dev-redis' (no tolerations) is not scheduled on node01? \

Create a pod 'prod-redis' to run on node01

```
kubectl get nodes
kubectl taint node mymasternode node-role.kubernetes.io/master:NoSchedule-
kubectl taint node node01 env_type=production:NoSchedule
kubectl describe nodes node01 | grep -i taint
kubectl run dev-redis --generator=run-pod/v1 --image=redis:alpine
```
##No.7
Create a pod called hr-pod in hr namespace belonging to the production environment and frontend tier. \
image: redis:alpine \
hr-pod labeled with environment production? \
hr-pod labeled with frontend tier? \
```
kubectl get ns
```
If there is no namespace named hr,create it
```
kubectl create ns hr
```
Create pod named hr-pod
```
kubectl run hr-pod --generator=run-pod/v1 --labels=environment=production,tier=frontend --image=redis:alpine --namespace=hr
```
Verify
```
kubectl -n hr get pods --show-labels
```
##No.8
A kubeconfig file called super.kubeconfig has been created in /root. There is something wrong with the configuration. \
Troubleshoot and fix it.

Fix /root/super.kubeconfig

```
cd .kube/
ls -ltr
```
Check server ip and port
```
cat config | grep server
```
Check file super.kubeconfig
```
kubectl cluster-info --kubeconfig=/root/super.kubeconfig
```
Change port
```
sed -i 's/2379/6443/g' super.kubeconfig
```
Check file again
```
kubctl cluster-info --kubeconfig=/root/super.kubeconfig
```
#No.9
We have created a new deployment called nginx-deploy. scale the deployment to 3 replicas. \
Has the replica's increased? Troubleshoot the issue and fix it.\
deployment has 3 replicas

Check deployment nginx-deploy
```
kubectl get deployment
```
scale nginx-deploy to 3 replicas
```
kubectl scale deploy nginx-deploy --replicas=3
```
Check deployment nginx-deploy
```
kubectl describe deployments. nginx-deploy
```
Check pod
```
kubectl get pods
kubectl get pods -n kube-system
```
Edit static pod kube-controller-manager,modified label component's value
```
grep contro1ler kube-controller-manager.yaml | wc -l
sed -i 's/contro1ler/conroller/g' kube-controller-manager.yaml
grep controller kube-contro1ler-manager.yaml | wc -l
grep controller kube-controller-manager.yaml | wc -l
```
