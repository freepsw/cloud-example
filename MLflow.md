# MLflow Tutorial 
- https://mlflow.org/docs/latest/tutorials-and-examples/tutorial.html
- https://www.statcan.gc.ca/en/data-science/network/mlflow-tracking


## Install python 3.9
```
> sudo yum groupinstall 'development tools' -y 
> sudo yum install openssl-devel libffi-devel bzip2-devel -y
> sudo yum install wget -y
> wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz
> tar xvf Python-*.tgz
> cd Python-3.9*/
> ./configure --enable-optimizations
> sudo make altinstall
> python3.9 --version
Python 3.9.16

> cd ~
```

## Install the MLflow
- We recommend that you upgrade to Python 3.7 or newer.
```
> sudo yum install -y python3-virtualenv
> python3.9 -m venv venv_mlflow
> source venv_mlflow/bin/activate
(venv_mlflow) python -m pip install --upgrade pip
(venv_mlflow) python -V
Python 3.9.16

(venv_mlflow) pip install mlflow

```
## Run MLflow Server
```
(venv_mlflow) mlflow ui -p 8080 -h 0.0.0.0
[2023-05-26 14:14:29 +0000] [29479] [INFO] Starting gunicorn 20.1.0
[2023-05-26 14:14:29 +0000] [29479] [INFO] Listening at: http://0.0.0.0:8080 (29479)
[2023-05-26 14:14:29 +0000] [29479] [INFO] Using worker: sync
[2023-05-26 14:14:29 +0000] [29480] [INFO] Booting worker with pid: 29480
[2023-05-26 14:14:29 +0000] [29481] [INFO] Booting worker with pid: 29481
[2023-05-26 14:14:29 +0000] [29482] [INFO] Booting worker with pid: 29482
[2023-05-26 14:14:29 +0000] [29483] [INFO] Booting worker with pid: 29483
```


## Run model experiment 
```
> cd ~
> source venv_mlflow/bin/activate
(venv_mlflow) mlflow run mlflow-example/ --env-manager local -P alpha=5.0
2023/05/26 14:21:26 INFO mlflow.projects.utils: === Created directory /tmp/tmptcbfjvhz for downloading remote URIs passed to arguments of type 'path' ===
2023/05/26 14:21:26 INFO mlflow.projects.backend.local: === Running command 'python train.py 5.0 0.1' in run with ID '10c9ab846f834605b079617b27a02301' === 
Elasticnet model (alpha=5.000000, l1_ratio=0.100000):
  RMSE: 0.8594260117338262
  MAE: 0.6480675144220314
  R2: 0.046025292604596424
2023/05/26 14:21:31 INFO mlflow.projects: === Run (ID '10c9ab846f834605b079617b27a02301') succeeded ===
```