# Scripts for cloud examples  

## 1. Run the http load test using hey tool (on ubuntu)
- https://github.com/rakyll/hey
```
sudo apt update
sudo apt install snapd
sudo snap install hey    
hey -z 20s -c 10 -n 1000 http://34.120.78.148
```


## 2. BigQuery Sample data
- https://github.com/datasets/house-prices-uk/blob/master/data/data.csv

```
Date	    Price (All)	Change (All)	Price (New)	Change (New)	Price (Modern)	Change (Modern)	Price (Older)	Change (Older)
1952-11-01	1891	    0.0	            2107	    0.0	2020	0.0	1524	0.0
1953-02-01	1891	    0.0	            2107	    0.0	2002	0.0	1542	0.0
1953-05-01	1891	    0.0	            2107	    0.0	2002	0.0	1542	0.0
1953-08-01	1881	    0.0	            2117	    0.0	2002	0.0	1524	0.0
```

### Query 
```sql
select primary_type , count(primary_type)
from bigquery-public-data.austin_crime.crime
group by primary_type
```

## 3. Google Cloud SDK 설치 (on CentOS 7)
- https://cloud.google.com/sdk/docs/downloads-yum?hl=ko

```
> sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-sdk]
name=Google Cloud SDK
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM

> sudo yum install google-cloud-sdk

> gcloud --version
Google Cloud SDK 305.0.0
alpha 2020.08.07
beta 2020.08.07
bq 2.0.58
core 2020.08.07
gsutil 4.52
kubectl 1.15.11

> gcloud init 


```

### Test gcloud command 
```
> gcloud config set account "freepsw.05@gmail.com"

> gcloud compute instances list
NAME               ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP   STATUS
gcloud-sdk-client  us-central1-a  n1-standard-1               10.128.0.10  34.69.189.78  RUNNING
```