from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def print_message(task_name):
    print(f"I'm in {task_name}")

default_args = {
    'owner': 'Ramesh S',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'My-Downstream-Task',
    default_args=default_args,
    description='A DAG to print messages for each task',
    schedule_interval=timedelta(days=1),
)

task_a = PythonOperator(
    task_id='task_a',
    python_callable=print_message,
    op_kwargs={'task_name': 'Task A'},
    dag=dag,
)

task_b = PythonOperator(
    task_id='task_b',
    python_callable=print_message,
    op_kwargs={'task_name': 'Task B'},
    dag=dag,
)

task_c = PythonOperator(
    task_id='task_c',
    python_callable=print_message,
    op_kwargs={'task_name': 'Task C'},
    dag=dag,
)

task_a >> task_b
task_a >> task_c
