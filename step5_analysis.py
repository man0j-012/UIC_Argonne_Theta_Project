# step5_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def analyze_failed_jobs_with_errors(failed_jobs_with_errors):
    # Number of unique failed jobs with associated hardware errors
    unique_failed_jobs = failed_jobs_with_errors['COBALT_JOBID'].nunique()
    print(f"Number of unique failed jobs with associated hardware errors: {unique_failed_jobs}")

    # Most common hardware errors in failed jobs
    common_errors = failed_jobs_with_errors['ERROR_MESSAGE'].value_counts().head(10)
    print("\nMost common hardware errors in failed jobs:")
    print(common_errors)

    # Plot the top 5 hardware errors
    common_errors.head(5).plot(kind='bar')
    plt.title('Top 5 Hardware Errors in Failed Jobs')
    plt.xlabel('Error Message')
    plt.ylabel('Count')
    plt.show()

def analyze_time_based_correlated_jobs(correlated_df):
    # Number of unique failed jobs with time-based correlated errors
    unique_failed_jobs = correlated_df['COBALT_JOBID'].nunique()
    print(f"Number of unique failed jobs with time-based correlated errors: {unique_failed_jobs}")

    # Most common hardware errors in time-based correlated jobs
    common_errors = correlated_df['ERROR_MESSAGE'].value_counts().head(10)
    print("\nMost common hardware errors in time-based correlated jobs:")
    print(common_errors)

    # Plot the top 5 hardware errors
    common_errors.head(5).plot(kind='bar')
    plt.title('Top 5 Hardware Errors in Time-Based Correlated Jobs')
    plt.xlabel('Error Message')
    plt.ylabel('Count')
    plt.show()

if __name__ == '__main__':
    # Load the correlated data
    failed_jobs_with_errors = pd.read_csv('failed_jobs_with_errors.csv', parse_dates=['START_TIMESTAMP', 'END_TIMESTAMP', 'EVENT_TIMESTAMP'])
    correlated_df = pd.read_csv('time_based_correlated_jobs.csv', parse_dates=['JOB_START', 'JOB_END', 'EVENT_TIMESTAMP'])

    # Analyze direct correlations
    print("Analyzing failed jobs with associated hardware errors via COBALT_JOBID...")
    analyze_failed_jobs_with_errors(failed_jobs_with_errors)

    # Analyze time-based correlations
    print("\nAnalyzing failed jobs with time-based correlated hardware errors...")
    analyze_time_based_correlated_jobs(correlated_df)
