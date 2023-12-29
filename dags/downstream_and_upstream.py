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

# ... (rest of the code remains unchanged)

# Create Task A with a PythonOperator
task_a = PythonOperator(
    task_id='task_a',
    python_callable=task_a_function,
    dag=dag,
)

# Create Task B with a PythonOperator
task_b = PythonOperator(
    task_id='task_b',
    python_callable=task_b_function,
    dag=dag,
)

# Create Task C with a PythonOperator
task_c = PythonOperator(
    task_id='task_c',
    python_callable=task_c_function,
    dag=dag,
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
