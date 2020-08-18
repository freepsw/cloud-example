from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# DAG 생성
my_dag = DAG(
    'my_dag',
    description='My First DAG',
    start_date=datetime(2019, 1, 1),
    schedule_interval='0 12 * * *',
    catchup=False
)

# 단순히 echo "Hello World (shell)" 명령을 실행하는 Task 생성
task_echo_hello_world = BashOperator(
    task_id='echo_hello_world',
    bash_command='echo "Hello World (shell)"',
    dag=my_dag)

def print_hello_world():
    return 'Hello World!!! (python)'

# 단순히 'Hello World!!! (python)'를 print 하는 Task 생성
task_print_hello_world = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello_world, # 위의 print_hello_world()
    dag=my_dag)

# 여기서 '>>'를 이용하여 순서를 정할 수 있습니다.
# task_echo_hello_world 테스크 실행 후에 task_print_hello_world를 실행하라는 의미입니다.
task_echo_hello_world >> task_print_hello_world
