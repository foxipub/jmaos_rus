cat ~/.kube/config | grep current | sed -e "s/current-context: //"
kubectl config current-context
