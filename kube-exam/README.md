

* [Site with test questions](https://marsforever.com/2020/01/22/CKA-with-Practice-Tests/)

# 1

Take a backup of the etcd cluster and save it to /opt/etcd-backup.db.

# 2

Create a Pod called redis-storage with image: redis:alpine with a Volume of type emptyDir that lasts for the life of the Pod.

Specs on the below:
Pod named 'redis-storage' created
Pod 'redis-storage' uses Volume type of emptyDir
Pod 'redis-storage' uses volumeMount with mountPath = /data/redis

# 3

Create a new pod called super-user-pod with image busybox:1.28. Allow the pod to be able to set system_time.

The container should sleep for 4800 seconds

Pod: super-user-pod
Container Image: busybox:1.28
SYS_TIME capabilities for the conatiner?

# 4

A pod definition file is created at /root/CKA/use-pv.yaml. Make use of this manifest file and mount the persistent volume called pv-1. Ensure the pod is running and the PV is bound.

mountPath: /data
persistentVolumeClaim Name: my-pvc

persistentVolume Claim configured correctly
pod using the correct mountPath
pod using the persistent volume claim?

Resources:

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: use-pv
  name: use-pv
spec:
  containers:
  - image: nginx
    name: use-pv
    volumeMounts:
      - mountPath: "/data"
        name: my-pv
  volumes:
    - name: my-pv
      persistentVolumeClaim:
        claimName: my-pvc
  dnsPolicy: ClusterFirst
  restartPolicy: Always
```

# 5

Create a new deployment called nginx-deploy, with image nginx:1.16 and 1 replica. Record the version. Next upgrade the deployment to version 1.17 using rolling update. Make sure that the version upgrade is recorded in the resource annotation.

Deployment : nginx-deploy. Image: nginx:1.16
Image: nginx:1.16
Task: Upgrade the version of the deployment to 1:17
Task: Record the changes for the image upgrade

# 6

Create a new user called john. Grant him access to the cluster. John should have permission to create, list, get, update and delete pods in the development namespace . The private key exists in the location: /root/CKA/john.key and csr at /root/CKA/john.csr.

Important Note: As of kubernetes 1.19, the CertificateSigningRequest object expects a signerName.

Please refer the documentation to see an example. The documentation tab is available at the top right of terminal.

CSR: john-developer Status:Approved
Role Name: developer, namespace: development, Resource: Pods
Access: User 'john' has appropriate permissions

Resources:

john.csr:

```
-----BEGIN CERTIFICATE REQUEST-----
MIICVDCCATwCAQAwDzENMAsGA1UEAwwEam9objCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBAJ5wBJstxfFUVKOBOTLdCKZNHm2GtOe2ATcmGe/IRp8Y6uM5
hftzctqQQmucXWHk7xL1SixlatPnOtwk/jFrfASgmS3fAHNV8Y340kbyU3RXoAO4
qw3k2A8PsTlFm+2R5XSuL4ZulfXLGiyQb9UcxwWKUMw+oWl4v1bKKLov1JOJM+KB
k78A0nsJ7E8btsEryYHMu4mOm4LM4bTS9MPfqieb+fZE7wdgZmv7tUwMAcE82qul
Sv44VOXTL+WYsn1mxef+uuhEquSJRtdICPtG142IM61Uib6zBWd4YIECcrHREYYt
P8sLA20AoJ1i7QpRtpVsArLEh8us3VR94fxKI6sCAwEAAaAAMA0GCSqGSIb3DQEB
CwUAA4IBAQAYAaUpoCGmLfKUkFweTkeiJGfkhB+Gv8FdiuYhAUWSf6Fk0npsT9aG
vEXCX8BVvnKpZV5r2CFrGi3olVqSa3rqTAJNBclzcrHqnE4a0Unbc6LwqM731Km3
/2FtvWYfzF0+bErCA4idqdbR9i4guFFtOvR4EilUNvD5R0SgTDimWP03yv9pSume
g40P/StwdyqXqUoA1riMwl2XqH0lOJd32t+upzcwEwn8Ry/vsbVFWROigDMYiA0g
SRkeuJM33xBZi/uYNsIQsm75YoEOz8M5CHjH06D3BSweoVtwt3gYPiMVJ3aIY721
XCA2yrh/IAjHkqBM9CMbDoH+MSZgNuE6
-----END CERTIFICATE REQUEST-----
```

john.key

```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAnnAEmy3F8VRUo4E5Mt0Ipk0ebYa057YBNyYZ78hGnxjq4zmF
+3Ny2pBCa5xdYeTvEvVKLGVq0+c63CT+MWt8BKCZLd8Ac1XxjfjSRvJTdFegA7ir
DeTYDw+xOUWb7ZHldK4vhm6V9csaLJBv1RzHBYpQzD6haXi/Vsooui/Uk4kz4oGT
vwDSewnsTxu2wSvJgcy7iY6bgszhtNL0w9+qJ5v59kTvB2Bma/u1TAwBwTzaq6VK
/jhU5dMv5ZiyfWbF5/666ESq5IlG10gI+0bXjYgzrVSJvrMFZ3hggQJysdERhi0/
ywsDbQCgnWLtClG2lWwCssSHy6zdVH3h/EojqwIDAQABAoIBAQCEYQgYOGiZOWL2
snP+QZyGhw0Tamgg6nudfqJRLL+FEya+8EM4U7/1Sm+UxjNoJgZziquM6LgXka4m
XmpdFHeszhrurtMLixWnD+1yBesg3E4Ajf2uQDUecHgdaEHef/Z+RUPESQXXNvoJ
ni0ynTbVNDpKTVJEc/U7KPJajrhJBBuajLfxikQYLSLnWITHeqbgT8q42DR0oJhD
CwwBcceAy+jMpFV+t96vlLAlmwWoZceFpWyxVd5kk3xs8GByfqACnn8capxqo3nf
BTD9/TOpfBC7R0P5xgPfEcdFb/OBlrJBZwhbr9dwQzS/eYJZG0gUvMuguYSxN0mP
nznnvuxRAoGBANGhOvKLbhO9yV4EEwxzgpQDNZ5csJI39QSH+W6fmp0W+PHYkBHo
oHArRuH2v3WY/kWIDoUlpQwf8RCf31hMmqR2RHqLcvBZ+t91sWh+mteZ8rSSQiHF
+nT2zZ2x35Pe66eLzniIF0uiKgPpYLJhpIY8Nz7wOr1m4tP3Q74bgAavAoGBAMF7
6OHIRNv+e6TtgZT08HTA77il36qgcI72UoegRgTfGiCjnX8zk2bJDepyEtT6whpy
rZrBru8mIDP4xvgX3768xSexQM43trXWMK5navrcnJoHM+IqNjbcHLhSY5j/mUHP
F2GQpsnPS52/SKyzZyjP5NPtv+mXjTzcaiV9urHFAoGAIYZod/umeg/DEX8TUM10
V5l/zLjEIE5EqBna4T8zKeZPn9XjjImohufU6TReAD+cgqA0ukR/9cVx9xeqT2PI
435qizKcCiZJwcz/t1dwCgT71LcDToVr/aKu1YZp3CstgtkQByS0nQrtLzz2kvCc
sD8XEsC2lC3NHtsPgWrCec8CgYAMaJDv4fMglLqDQkQcNHUzV6hIFEM64x003fE/
B3VWHKTFURjprnoWjnBZB8XTaN2H6rDdiuxYI/7Otna0NHvB9MNEH2cDkqkiEkF+
/dzrh7h3XFzkdUaS0Bz7aTU/+6xtfwWF2UwJB0VXMYxMnxjPkj2fpdC3/2MscwpP
qzeM7QKBgQCLWy1YqkRONskzafuHaPzK+4YxvX++NGti/lev6OKuvOABSXT8gVQr
m+MOpUGWLMMFaDX3bEvqWaqOhGv58+9hd29a2vY4R/vl3jfeEz5G3ut3hyxDSCGE
S1bz58IVkgaOBQrqbe1dn6koHtlgPqV9sD/zMCAbR6RVf7J4pGR6Ew==
-----END RSA PRIVATE KEY-----
```

# 7

Create a nginx pod called nginx-resolver using image nginx, expose it internally with a service called nginx-resolver-service. Test that you are able to look up the service and pod names from within the cluster. Use the image: busybox:1.28 for dns lookup. Record results in /root/CKA/nginx.svc and /root/CKA/nginx.pod

Pod: nginx-resolver created
Service DNS Resolution recorded correctly
Pod DNS resolution recorded correctly

# 8

Create a static pod on node01 called nginx-critical with image nginx and make sure that it is recreated/restarted automatically in case of a failure.

Use /etc/kubernetes/manifests as the Static Pod path for example.

static pod configured under /etc/kubernetes/manifests ?
Pod nginx-critical-node01 is up and running