# step4_time_based_correlation.py

import pandas as pd
from tqdm import tqdm

def time_based_correlation(failed_jobs_no_errors, hardware_error_log):
    # Ensure timestamps are datetime and timezone-aware
    failed_jobs_no_errors['START_TIMESTAMP'] = pd.to_datetime(failed_jobs_no_errors['START_TIMESTAMP'])
    failed_jobs_no_errors['END_TIMESTAMP'] = pd.to_datetime(failed_jobs_no_errors['END_TIMESTAMP'])
    hardware_error_log['EVENT_TIMESTAMP'] = pd.to_datetime(hardware_error_log['EVENT_TIMESTAMP'])

    # Convert timestamps to UTC if they are timezone-aware
    failed_jobs_no_errors['START_TIMESTAMP'] = failed_jobs_no_errors['START_TIMESTAMP'].dt.tz_convert('UTC')
    failed_jobs_no_errors['END_TIMESTAMP'] = failed_jobs_no_errors['END_TIMESTAMP'].dt.tz_convert('UTC')
    hardware_error_log['EVENT_TIMESTAMP'] = hardware_error_log['EVENT_TIMESTAMP'].dt.tz_convert('UTC')

    # Ensure that EVENT_TIMESTAMP is the index for efficient time-based operations
    hardware_error_log.set_index('EVENT_TIMESTAMP', inplace=True)

    # Sort the index to enable slicing
    hardware_error_log.sort_index(inplace=True)

    # Initialize a list to store correlation results
    correlation_results = []

    # Iterate over each failed job without associated hardware errors
    for idx, job in tqdm(failed_jobs_no_errors.iterrows(), total=failed_jobs_no_errors.shape[0], desc="Processing jobs"):
        # Get the job's start and end times
        start_time = job['START_TIMESTAMP']
        end_time = job['END_TIMESTAMP']

        # Ensure start_time and end_time are timezone-aware and in UTC
        start_time = start_time.tz_convert('UTC')
        end_time = end_time.tz_convert('UTC')

        # Get errors that occurred during the job's execution time
        try:
            overlapping_errors = hardware_error_log.loc[start_time:end_time]
        except KeyError:
            # If the timestamps are outside the index range, continue
            continue

        if not overlapping_errors.empty:
            for error_idx, error in overlapping_errors.iterrows():
                correlation_results.append({
                    'COBALT_JOBID': job['COBALT_JOBID'],
                    'JOB_START': start_time,
                    'JOB_END': end_time,
                    'EXIT_STATUS': job['EXIT_STATUS'],
                    'EVENT_TIMESTAMP': error_idx,
                    'ERROR_MESSAGE': error['ERROR_MESSAGE'],
                    'COMPONENT_NAME': error['COMPONENT_NAME'],
                    'ERROR_CODE': error['ERROR_CODE'],
                    'ERROR_CATEGORY_STRING': error['ERROR_CATEGORY_STRING']
                })

    # Convert the results to a DataFrame
    correlated_df = pd.DataFrame(correlation_results)

    return correlated_df

if __name__ == '__main__':
    # Load preprocessed data
    job_log = pd.read_csv('preprocessed_job_log.csv', parse_dates=['START_TIMESTAMP', 'END_TIMESTAMP'])
    hardware_error_log = pd.read_csv('preprocessed_hardware_error_log.csv', parse_dates=['EVENT_TIMESTAMP'])

    # Load failed jobs with associated hardware errors via COBALT_JOBID
    failed_jobs_with_errors = pd.read_csv('failed_jobs_with_errors.csv', parse_dates=['START_TIMESTAMP', 'END_TIMESTAMP', 'EVENT_TIMESTAMP'])

    # Identify failed jobs without associated hardware errors
    failed_job_ids_with_errors = failed_jobs_with_errors['COBALT_JOBID'].unique()
    failed_jobs_no_errors = job_log[
        (job_log['EXIT_STATUS'] != 0) & (~job_log['COBALT_JOBID'].isin(failed_job_ids_with_errors))
    ].copy()

    print(f"Number of failed jobs without associated hardware errors: {len(failed_jobs_no_errors)}")

    # Perform time-based correlation
    correlated_df = time_based_correlation(failed_jobs_no_errors, hardware_error_log)

    # Save the results
    correlated_df.to_csv('time_based_correlated_jobs.csv', index=False)

    print(f"\nNumber of time-based correlated job-error pairs: {len(correlated_df)}")
    print("\nSample of time-based correlated data:")
    print(correlated_df.head())
