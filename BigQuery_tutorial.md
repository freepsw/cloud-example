# BigQuery Tutorials

## Prerequisit


https://github.com/googleapis/python-bigquery-reservation
```
- Select or create a Cloud Platform project.
- Enable billing for your project.
- Enable the Cloud BigQuery Reservation API.
- Setup Authentication.
```


### Set up virtual env 
### Anaconda vs. Miniconda vs. Virtualenv
- https://deeplearning.lipingyang.org/2018/12/23/anaconda-vs-miniconda-vs-virtualenv/
- https://stackoverflow.com/questions/38217545/what-is-the-difference-between-pyenv-virtualenv-anaconda

#### Anaconda
- python과 관련된 모든 어플리케이션, 패키지 등을 자동으로 설치
- 약 720개 이상의 package들을 자동으로 설치해 줌. 
- 최소 3G 이상의 디스크 공간 필요  

#### Miniconda 
- python package를 관리하기 위한 용도로 최적화
- Anaconda에서 제공하는 다양한 어플리케이션은 설치되지 않음
- 단순히 python 가상환경을 구성하여 프로그래밍하는 목적으로 최적
- 디스크 사용량 최소화 (다만 필요한 패키지는 직접 설치)

##### Virtualenv
- python 버전별로 별도의 python 가상환경을 제공하는 용도
    - pyenv는 python 버전 별로 환경을 제공했다면, (동일 package의 다른 버전 설치시 관리 어려움)
    - virtualenv는 동일한 python 버전이라도,
    - 프로젝트에 따라 동일한 package의 다른 버전을 설치할 수 있도록 지원
- sudo(관리자 권한)이 있는 경우에만 사용 가능함. 
- conda 보다 복잡한 명령어 이해와 관리가 필요

#### pyenv
- python 버전을 쉽게 설치 및 변경할 수 있게 지원
- 동일한 버전의 python에 서로 다른 버전의 package(numpy 등)을 설치하면
- 버전 호환등의 문제로 실행시 오류가 발생하는 이슈 (사용자가 직접 관리해야 함)
    - 즉, 완벽한 독립적인 가상환경을 제공하지는 못함. 
- windows는 지원하지 않음


### Set up python virtual env
```
> pip install virtualenv
> virtualenv venv_bigquery --python=python3.8
> source venv_cloud/bin/activate
> python -V  
Python 3.8.2
```