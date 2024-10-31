# step1_load_data.py

import pandas as pd

def load_data(job_logs_path, hardware_errors_path):
    """
    Loads the job logs and hardware error logs into pandas DataFrames.
    """
    # Load Job Logs
    print("Loading Job Logs...")
    job_log = pd.read_csv(job_logs_path, parse_dates=['START_TIMESTAMP', 'END_TIMESTAMP'])

    # Load Hardware Error Logs
    print("Loading Hardware Error Logs...")
    hardware_error_log = pd.read_csv(hardware_errors_path, parse_dates=['EVENT_TIMESTAMP'])

    return job_log, hardware_error_log

if __name__ == '__main__':
    # Specify the paths to your CSV files
    job_logs_path = 'C:/Users/dattu/OneDrive/Desktop/UIC_Argonne_Theta_Project/job_logs_2019.csv'
    hardware_errors_path = 'C:/Users/dattu/OneDrive/Desktop/UIC_Argonne_Theta_Project/hardware_errors_2019_cleaned.csv'

    # Call the load_data function
    job_log, hardware_error_log = load_data(job_logs_path, hardware_errors_path)
