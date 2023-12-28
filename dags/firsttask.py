from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define a simple Python function for Task A
def task_a_function():
    print("Executing Task A")

# Define a simple Python function for Task B
def task_b_function():
    print("Executing Task B")

# Define a simple Python function for Task C
def task_c_function():
    print("Executing Task C")

# Define default arguments for the DAG
default_args = {
    'owner': 'Ramesh',                # Owner of the DAG
    'start_date': datetime(2023, 1, 1), # Start date for the DAG
    'retries': 1,                       # Number of retries for each task
    'retry_delay': timedelta(minutes=1),# Delay between retries
}

# Create a DAG instance
dag = DAG(
    'first_example_DAG',                      # Unique identifier for the DAG
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

# Define the execution sequence (Task A -> Task B -> Task C)
task_a >> task_b >> task_c


# Here's a step-by-step explanation:
# * Task A will be executed first.
# * Once Task A completes successfully, Task B will be triggered.
# * Task B will wait for the successful completion of Task A before starting.
# * After Task B completes successfully, Task C will be triggered.
# * Task C will wait for the successful completion of Task B before starting.
