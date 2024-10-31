# step2_preprocess_data.py

import pandas as pd

def standardize_timestamps(job_log, hardware_error_log):
    # Convert to datetime if not already done
    job_log['START_TIMESTAMP'] = pd.to_datetime(job_log['START_TIMESTAMP'])
    job_log['END_TIMESTAMP'] = pd.to_datetime(job_log['END_TIMESTAMP'])
    hardware_error_log['EVENT_TIMESTAMP'] = pd.to_datetime(hardware_error_log['EVENT_TIMESTAMP'])

    # Localize timestamps to UTC if they are timezone-naive
    if job_log['START_TIMESTAMP'].dt.tz is None:
        job_log['START_TIMESTAMP'] = job_log['START_TIMESTAMP'].dt.tz_localize('UTC')
    if job_log['END_TIMESTAMP'].dt.tz is None:
        job_log['END_TIMESTAMP'] = job_log['END_TIMESTAMP'].dt.tz_localize('UTC')
    if hardware_error_log['EVENT_TIMESTAMP'].dt.tz is None:
        hardware_error_log['EVENT_TIMESTAMP'] = hardware_error_log['EVENT_TIMESTAMP'].dt.tz_localize('UTC')

    return job_log, hardware_error_log

def handle_missing_values(job_log, hardware_error_log):
    # Drop rows with missing critical information in job logs
    job_log_cleaned = job_log.dropna(subset=['COBALT_JOBID', 'START_TIMESTAMP', 'END_TIMESTAMP', 'LOCATION', 'EXIT_STATUS']).copy()

    # Drop rows with missing critical information in hardware error logs
    hardware_error_log_cleaned = hardware_error_log.dropna(subset=['EVENT_TIMESTAMP', 'COMPONENT_NAME', 'FAILED_COMPONENT']).copy()

    return job_log_cleaned, hardware_error_log_cleaned

def ensure_correct_data_types(job_log, hardware_error_log):
    # For job logs
    job_log.loc[:, 'COBALT_JOBID'] = job_log['COBALT_JOBID'].astype(int)
    job_log.loc[:, 'EXIT_STATUS'] = job_log['EXIT_STATUS'].astype(int)

    # For hardware error logs
    hardware_error_log.loc[:, 'FAILED_COMPONENT'] = hardware_error_log['FAILED_COMPONENT'].astype(int)

    return job_log, hardware_error_log

def preprocess_data(job_log, hardware_error_log):
    print("Standardizing timestamps...")
    job_log, hardware_error_log = standardize_timestamps(job_log, hardware_error_log)

    print("Handling missing values...")
    job_log, hardware_error_log = handle_missing_values(job_log, hardware_error_log)

    print("Ensuring correct data types...")
    job_log, hardware_error_log = ensure_correct_data_types(job_log, hardware_error_log)

    return job_log, hardware_error_log

if __name__ == '__main__':
    from step1_load_data import load_data

    # Specify the paths to your CSV files
    job_logs_path = 'C:/Users/dattu/OneDrive/Desktop/UIC_Argonne_Theta_Project/job_logs_2019.csv'
    hardware_errors_path = 'C:/Users/dattu/OneDrive/Desktop/UIC_Argonne_Theta_Project/hardware_errors_2019_cleaned.csv'

    # Load data
    job_log, hardware_error_log = load_data(job_logs_path, hardware_errors_path)

    # Preprocess data
    job_log, hardware_error_log = preprocess_data(job_log, hardware_error_log)

    # Save preprocessed data for later use
    job_log.to_csv('preprocessed_job_log.csv', index=False)
    hardware_error_log.to_csv('preprocessed_hardware_error_log.csv', index=False)
