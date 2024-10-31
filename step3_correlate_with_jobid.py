# step3_correlate_with_jobid.py

import pandas as pd

def correlate_with_jobid(job_log, hardware_error_log):
    # Filter hardware errors with non-null COBALT_JOBID
    errors_with_jobid = hardware_error_log.dropna(subset=['COBALT_JOBID']).copy()

    # Ensure COBALT_JOBID is an integer in both DataFrames
    errors_with_jobid['COBALT_JOBID'] = errors_with_jobid['COBALT_JOBID'].astype(int)

    # Merge job logs and hardware errors on COBALT_JOBID
    merged_on_jobid = pd.merge(
        job_log,
        errors_with_jobid,
        on='COBALT_JOBID',
        how='inner',
        suffixes=('_job', '_error')
    )

    # Identify failed jobs with associated hardware errors
    failed_jobs_with_errors = merged_on_jobid[merged_on_jobid['EXIT_STATUS'] != 0]

    return failed_jobs_with_errors

if __name__ == '__main__':
    # Load preprocessed data
    job_log = pd.read_csv('preprocessed_job_log.csv', parse_dates=['START_TIMESTAMP', 'END_TIMESTAMP'])
    hardware_error_log = pd.read_csv('preprocessed_hardware_error_log.csv', parse_dates=['EVENT_TIMESTAMP'])

    # Perform correlation
    failed_jobs_with_errors = correlate_with_jobid(job_log, hardware_error_log)

    # Save the results
    failed_jobs_with_errors.to_csv('failed_jobs_with_errors.csv', index=False)

    # Print some information
    print(f"Number of failed jobs with associated hardware errors: {len(failed_jobs_with_errors)}")
    print("\nSample of failed jobs with associated hardware errors:")
    print(failed_jobs_with_errors[['COBALT_JOBID', 'EXIT_STATUS', 'ERROR_MESSAGE']].head())
