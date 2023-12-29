from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG

# Define a simple Python function for Task A
def task_a_function():
    print("Executing Task A")

# Define a simple Python function for Task B
def task_b_function():
    print("Executing Task B")

# Define a simple Python function for Task C
def task_c_function():
    print("Executing Task C")

# Define a simple Python function for Task D
def task_d_function():
    print("Executing Task D")

# Define a simple Python function for Task E
def task_e_function():
    print("Executing Task E")

# Define default arguments for the DAG
default_args = {
    'owner': 'Ramesh',                # Owner of the DAG
    'start_date': datetime(2023, 1, 1), # Start date for the DAG
    'retries': 1,                       # Number of retries for each task
    'retry_delay': timedelta(minutes=1),# Delay between retries
}

# Create a DAG instance
dag = DAG(
    'Upstream_DownStream_Example',                # Unique identifier for the DAG
    default_args=default_args,          # Default arguments
    description='A simple example DAG', # Description of the DAG
    schedule_interval=timedelta(days=1),# Schedule interval for DAG runs (daily in this case)
)

# Create Task A with a PythonOperator
task_a = PythonOperator(
    task_id='task_a',                   # Unique identifier for the task
    python_callable=task_a_function,    # Python function to be executed
    dag=dag,                            # Associated DAG
)

# Create Task B with a PythonOperator
task_b = PythonOperator(
    task_id='task_b',                   # Unique identifier for the task
    python_callable=task_b_function,    # Python function to be executed
    dag=dag,                            # Associated DAG
)

# Create Task C with a PythonOperator
task_c = PythonOperator(
    task_id='task_c',                   # Unique identifier for the task
    python_callable=task_c_function,    # Python function to be executed
    dag=dag,                            # Associated DAG
)

# Create Task D with a PythonOperator
task_d = PythonOperator(
    task_id='task_d',
    python_callable=task_d_function,
    dag=dag,
)

# Create Task E with a PythonOperator
task_e = PythonOperator(
    task_id='task_e',
    python_callable=task_e_function,
    dag=dag,
)

# Execution sequence: Task A -> Task B -> Task C -> Task D -> Task E
task_a >> task_b >> task_c >> task_d >> task_e

# Execution sequence with comments:
# Task A triggers Task B and Task C in parallel
# Task B triggers Task D and Task E in parallel
# Task C triggers Task D and Task E in parallel
task_a >> [task_b, task_c]
task_b >> [task_d, task_e]
task_c >> [task_d, task_e]
