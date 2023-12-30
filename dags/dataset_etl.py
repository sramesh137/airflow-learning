# This Airflow DAG consists of two tasks: 
# one for selecting specific columns from the dataset and another for printing the processed data.
#  The tasks are scheduled to run daily, and the print_processed_data_task depends on the successful completion of the select_columns_task.

# Import Libraries:

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import logging, os, sys

# Configure logging to output messages to both the console and a log file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Log to console
        logging.FileHandler('/opt/airflow/logs/logfile.log')
    ]
)

# Step 1: Define the processing function to select columns
# Define the select_columns Function: This function reads a CSV dataset (ds_salaries.csv), selects specific columns (experience_level, job_title, salary_in_usd, company_location), and saves the processed data to a new CSV file (selected_columns_dataset.csv).
def select_columns(dataset_path):
    try:
        
        # Load the dataset
        dataset_path = '/opt/airflow/dags/ds_salaries.csv'
        df = pd.read_csv(dataset_path)

        # Select only the desired columns
        selected_columns = ['experience_level', 'job_title', 'salary_in_usd', 'company_location']
        df_processed = df[selected_columns]

        # Save the processed data to a new location
        processed_dataset_path = '/opt/airflow/dags/result_ds.csv'
        df_processed.to_csv(processed_dataset_path, index=False)

    # error handling to print an error message if any issues occur during column selection.
        logging.info("Step 1: Selected columns successfully.")
    except Exception as e:
        logging.error(f"Error in selecting columns: {str(e)}",exc_info=True)

# Step 2: Define the processing function to print the processed data
# This function reads the processed dataset (selected_columns_dataset.csv) and prints the first few rows.
def print_processed_data():
    try:
        # Load the processed dataset
        processed_dataset_path = '/opt/airflow/dags/result_ds.csv'
        df_processed = pd.read_csv(processed_dataset_path)

        # Print the processed data
        logging.info("Step 2: Processed Dataset:")
        logging.info(df_processed.head())
    # It includes error handling to print an error message if any issues occur during data printing.        
    except Exception as e:
        logging.error(f"Error in printing processed data: {str(e)}")

# Step 3: Define default arguments for the DAG
# Set default arguments for the Airflow DAG, including the owner, start date, and retry configuration.
default_args = {
    'owner': 'Ramesh S-test',
    'start_date': datetime(2023, 1, 1, 2),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Step 4: Create a DAG instance
# Create a DAG instance named 'process_static_dataset' with the specified default arguments, description, and a daily schedule interval.
dag = DAG(
    'process_static_dataset-ds',
    default_args=default_args,
    description='DAG for processing a static dataset',
    schedule_interval=timedelta(days=1),
    # timezone=local_timezone,
)

# Step 5: Define tasks for each processing step
# select_columns_task = PythonOperator(
#     task_id='select_columns_task',
#     python_callable=select_columns,
#     dag=dag,
# )

select_columns_task = PythonOperator(
    task_id='select_columns_task',
    python_callable=select_columns,
    op_kwargs={'dataset_path': '/opt/airflow/dags/ds_salaries.csv'},
    dag=dag,
)


print_processed_data_task = PythonOperator(
    task_id='print_processed_data_task',
    python_callable=print_processed_data,
    dag=dag,
)

# Step 6: Set up dependencies
# Set up a dependency between the two tasks, where print_processed_data_task depends on the successful execution of select_columns_task.
select_columns_task >> print_processed_data_task

if __name__ == "__main__":
    try:
        dag.cli()
        logging.info("DAG execution completed successfully.")
    except Exception as e:
        logging.error(f"Error running DAG: {str(e)}")