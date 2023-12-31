## Apache Airflow Tutorial
This tutorial provides a step-by-step guide to getting started with Apache Airflow, an open-source platform used for orchestrating and scheduling workflows.

Table of Contents
- [Introduction](#Introduction)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Examples](#Examples)

# Introduction
In this tutorial, you will learn the basics of Apache Airflow and how to use it to create and manage workflows. Airflow allows you to define complex workflows as Directed Acyclic Graphs (DAGs), which consist of tasks and dependencies between them. These workflows can be scheduled, monitored, and managed through a web-based user interface.

### Prerequisites
Before getting started with Apache Airflow, make sure you have the following prerequisites:

1. Python (version 3.6.x or higher) installed
2. Basic understanding of Python and programming concepts
3. Familiarity with command-line interface (CLI)
4. Access to a terminal or command prompt
5. Version Control (e.g., Git)

Resources
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Apache Airflow GitHub Repository](https://github.com/apache/airflow)

# Installation

## Deploying a Apache Airflow using on docker.
1. Install Docker Desktop for mac (https://docs.docker.com/desktop/install/mac-install/)
2. fetch docker-compose.yaml (https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'
```
3. Create below subdirectories
```
mkdir -p ./dags ./logs ./plugins ./config
```
4. Initialize the airflow database
```
docker compose up airflow-init
```
5. Start Docker containers defined in a Docker Compose file in detached mode. Means, start the defined services in the background.
```
-> docker compose up -d
[+] Running 5/5
 ✔ Container docker-airflow-postgres-1           Healthy                                                                                                                                          0.0s 
 ✔ Container docker-airflow-airflow-init-1       Started                                                                                                                                          0.0s 
 ✔ Container docker-airflow-airflow-scheduler-1  Running                                                                                                                                          0.0s 
 ✔ Container docker-airflow-airflow-triggerer-1  Running                                                                                                                                          0.0s 
 ✔ Container docker-airflow-airflow-webserver-1  Running                                                                                                                                          0.0s 
```
6. List the currently running Docker containers
```
➜  docker ps -a

CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                      PORTS                    NAMES
eef8b236a1c4   apache/airflow:2.8.0   "/usr/bin/dumb-init …"   18 minutes ago   Exited (2) 17 minutes ago                            docker-airflow-flower-1
bf6bbc0ba723   apache/airflow:2.8.0   "/usr/bin/dumb-init …"   46 hours ago     Up 16 minutes (healthy)     0.0.0.0:8080->8080/tcp   docker-airflow-airflow-webserver-1
f37f1e05990c   apache/airflow:2.8.0   "/usr/bin/dumb-init …"   46 hours ago     Up 16 minutes (healthy)     8080/tcp                 docker-airflow-airflow-scheduler-1
29c43530b4a6   apache/airflow:2.8.0   "/usr/bin/dumb-init …"   46 hours ago     Up 16 minutes (healthy)     8080/tcp                 docker-airflow-airflow-triggerer-1
02b30cdc6852   apache/airflow:2.8.0   "/bin/bash -c 'if [[…"   46 hours ago     Exited (0) 2 minutes ago                             docker-airflow-airflow-init-1
cacade54f3d3   postgres:13            "docker-entrypoint.s…"   46 hours ago     Up 16 minutes (healthy)     5432/tcp                 docker-airflow-postgres-1
```

# Examples
## firsttask.py - Graph flow
<img width="698" alt="Screenshot 2023-12-29 at 10 20 12 AM" src="https://github.com/sramesh137/airflow-learning/assets/88080444/25c900d7-e64f-4bb2-a39b-5e9245fac93c">

## downstream_and_upstream.py - Graph flow
<img width="1132" alt="Screenshot 2023-12-29 at 10 22 14 AM" src="https://github.com/sramesh137/airflow-learning/assets/88080444/2eb2332d-2266-4db2-ae6e-6ea43df0f5b4">

## dataset_etl.py - Graph flow
<img width="478" alt="Screenshot 2023-12-30 at 12 22 14 PM" src="https://github.com/sramesh137/airflow-learning/assets/88080444/3000ccb4-5435-465f-9738-3fbc814f4abc">

#### Logs for the first task
```
*** Found local files:
***   * /opt/airflow/logs/dag_id=process_static_dataset-ds/run_id=manual__2023-12-29T16:43:01.921567+00:00/task_id=select_columns_task/attempt=1.log
[2023-12-29, 16:43:02 UTC] {taskinstance.py:1957} INFO - Dependencies all met for dep_context=non-requeueable deps ti=<TaskInstance: process_static_dataset-ds.select_columns_task manual__2023-12-29T16:43:01.921567+00:00 [queued]>
[2023-12-29, 16:43:02 UTC] {taskinstance.py:1957} INFO - Dependencies all met for dep_context=requeueable deps ti=<TaskInstance: process_static_dataset-ds.select_columns_task manual__2023-12-29T16:43:01.921567+00:00 [queued]>
[2023-12-29, 16:43:02 UTC] {taskinstance.py:2171} INFO - Starting attempt 1 of 2
[2023-12-29, 16:43:02 UTC] {taskinstance.py:2192} INFO - Executing <Task(PythonOperator): select_columns_task> on 2023-12-29 16:43:01.921567+00:00
[2023-12-29, 16:43:02 UTC] {standard_task_runner.py:60} INFO - Started process 950 to run task
[2023-12-29, 16:43:02 UTC] {standard_task_runner.py:87} INFO - Running: ['***', 'tasks', 'run', 'process_static_dataset-ds', 'select_columns_task', 'manual__2023-12-29T16:43:01.921567+00:00', '--job-id', '135', '--raw', '--subdir', 'DAGS_FOLDER/dataset_etl.py', '--cfg-path', '/tmp/tmpedvl3npo']
[2023-12-29, 16:43:02 UTC] {standard_task_runner.py:88} INFO - Job 135: Subtask select_columns_task
[2023-12-29, 16:43:02 UTC] {task_command.py:423} INFO - Running <TaskInstance: process_static_dataset-ds.select_columns_task manual__2023-12-29T16:43:01.921567+00:00 [running]> on host f37f1e05990c
[2023-12-29, 16:43:02 UTC] {taskinstance.py:2481} INFO - Exporting env vars: AIRFLOW_CTX_DAG_OWNER='Ramesh S-test' AIRFLOW_CTX_DAG_ID='process_static_dataset-ds' AIRFLOW_CTX_TASK_ID='select_columns_task' AIRFLOW_CTX_EXECUTION_DATE='2023-12-29T16:43:01.921567+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='manual__2023-12-29T16:43:01.921567+00:00'
[2023-12-29, 16:43:02 UTC] {dataset_etl.py:41} INFO - Step 1: Selected columns successfully.
[2023-12-29, 16:43:02 UTC] {python.py:201} INFO - Done. Returned value was: None
[2023-12-29, 16:43:02 UTC] {taskinstance.py:1138} INFO - Marking task as SUCCESS. dag_id=process_static_dataset-ds, task_id=select_columns_task, execution_date=20231229T164301, start_date=20231229T164302, end_date=20231229T164302
[2023-12-29, 16:43:03 UTC] {local_task_job_runner.py:234} INFO - Task exited with return code 0
[2023-12-29, 16:43:03 UTC] {taskinstance.py:3281} INFO - 1 downstream tasks scheduled from follow-on schedule check
```

#### Logs for the second task
```
*** Found local files:
***   * /opt/airflow/logs/dag_id=process_static_dataset-ds/run_id=manual__2023-12-29T16:43:01.921567+00:00/task_id=print_processed_data_task/attempt=1.log
[2023-12-29, 16:43:03 UTC] {taskinstance.py:1957} INFO - Dependencies all met for dep_context=non-requeueable deps ti=<TaskInstance: process_static_dataset-ds.print_processed_data_task manual__2023-12-29T16:43:01.921567+00:00 [queued]>
[2023-12-29, 16:43:03 UTC] {taskinstance.py:1957} INFO - Dependencies all met for dep_context=requeueable deps ti=<TaskInstance: process_static_dataset-ds.print_processed_data_task manual__2023-12-29T16:43:01.921567+00:00 [queued]>
[2023-12-29, 16:43:03 UTC] {taskinstance.py:2171} INFO - Starting attempt 1 of 2
[2023-12-29, 16:43:03 UTC] {taskinstance.py:2192} INFO - Executing <Task(PythonOperator): print_processed_data_task> on 2023-12-29 16:43:01.921567+00:00
[2023-12-29, 16:43:03 UTC] {standard_task_runner.py:60} INFO - Started process 985 to run task
[2023-12-29, 16:43:03 UTC] {standard_task_runner.py:87} INFO - Running: ['***', 'tasks', 'run', 'process_static_dataset-ds', 'print_processed_data_task', 'manual__2023-12-29T16:43:01.921567+00:00', '--job-id', '146', '--raw', '--subdir', 'DAGS_FOLDER/dataset_etl.py', '--cfg-path', '/tmp/tmptn_mbeyh']
[2023-12-29, 16:43:03 UTC] {standard_task_runner.py:88} INFO - Job 146: Subtask print_processed_data_task
[2023-12-29, 16:43:03 UTC] {task_command.py:423} INFO - Running <TaskInstance: process_static_dataset-ds.print_processed_data_task manual__2023-12-29T16:43:01.921567+00:00 [running]> on host f37f1e05990c
[2023-12-29, 16:43:04 UTC] {taskinstance.py:2481} INFO - Exporting env vars: AIRFLOW_CTX_DAG_OWNER='Ramesh S-test' AIRFLOW_CTX_DAG_ID='process_static_dataset-ds' AIRFLOW_CTX_TASK_ID='print_processed_data_task' AIRFLOW_CTX_EXECUTION_DATE='2023-12-29T16:43:01.921567+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='manual__2023-12-29T16:43:01.921567+00:00'
[2023-12-29, 16:43:04 UTC] {dataset_etl.py:54} INFO - Step 2: Processed Dataset:
[2023-12-29, 16:43:04 UTC] {dataset_etl.py:55} INFO -
                experience_level   job_title  salary_in_usd company_location
0               SE  Principal Data Scientist          85847               ES
1               MI               ML Engineer          30000               US
2               MI               ML Engineer          25500               US
3               SE            Data Scientist         175000               CA
4               SE            Data Scientist         120000               CA
[2023-12-29, 16:43:04 UTC] {python.py:201} INFO - Done. Returned value was: None
[2023-12-29, 16:43:04 UTC] {taskinstance.py:1138} INFO - Marking task as SUCCESS. dag_id=process_static_dataset-ds, task_id=print_processed_data_task, execution_date=20231229T164301, start_date=20231229T164303, end_date=20231229T164304
[2023-12-29, 16:43:04 UTC] {local_task_job_runner.py:234} INFO - Task exited with return code 0
[2023-12-29, 16:43:04 UTC] {taskinstance.py:3281} INFO - 0 downstream tasks scheduled from follow-on schedule check
```
