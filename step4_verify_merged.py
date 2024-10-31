import pandas as pd

# Path to your merged DataFrame
merged_data_path = 'C:/Users/dattu/OneDrive/Desktop/UIC_Argonne_Theta_Project/merged_hardware_job_logs_2019.csv'  # Update if your path is different

# Load the merged DataFrame
print("Loading Merged Hardware and Job Logs...")
merged_df = pd.read_csv(merged_data_path, parse_dates=['EVENT_TIMESTAMP', 'START_TIMESTAMP', 'END_TIMESTAMP', 'QUEUED_TIMESTAMP'])

# 1. List all column names
print("\nList of Columns in Merged DataFrame:")
print(merged_df.columns.tolist())

# 2. Check for any missing values in key columns
key_columns = ['COBALT_JOBID', 'EVENT_TIMESTAMP', 'COMPONENT_NAME', 'JOB_NAME', 'LOCATION']
print("\nMissing Values in Key Columns:")
print(merged_df[key_columns].isnull().sum())

# 3. Display data types of key columns
print("\nData Types of Key Columns:")
print(merged_df[key_columns].dtypes)

# 4. Display the first few rows to inspect sample data
print("\nSample Data from Merged DataFrame:")
print(merged_df[key_columns].head(10))

# 5. Check the number of unique COBALT_JOBIDs to ensure they match between datasets
unique_jobids_merged = merged_df['COBALT_JOBID'].nunique()
print(f"\nNumber of Unique COBALT_JOBID in Merged DataFrame: {unique_jobids_merged}")

# Optional: Compare with original Job Logs
job_logs_path = 'C:/Users/dattu/OneDrive/Desktop/UIC_Argonne_Theta_Project/job_logs_2019.csv'  # Ensure this path is correct
job_log = pd.read_csv(job_logs_path)
unique_jobids_job_log = job_log['COBALT_JOBID'].nunique()
print(f"Number of Unique COBALT_JOBID in Job Logs: {unique_jobids_job_log}")

# 6. Verify that the number of non-null COBALT_JOBIDs in merged data matches expectations
total_hardware_errors = len(merged_df)
assigned_jobids = merged_df['COBALT_JOBID'].notnull().sum()
print(f"\nTotal Hardware Errors: {total_hardware_errors}")
print(f"Hardware Errors Assigned a COBALT_JOBID: {assigned_jobids}")
print(f"Hardware Errors Without a COBALT_JOBID: {merged_df['COBALT_JOBID'].isnull().sum()}")

# 7. Save a brief verification report (optional)
verification_report = {
    'Total Hardware Errors': total_hardware_errors,
    'Assigned COBALT_JOBIDs': assigned_jobids,
    'Missing COBALT_JOBIDs': merged_df['COBALT_JOBID'].isnull().sum(),
    'Unique COBALT_JOBIDs in Merged Data': unique_jobids_merged,
    'Unique COBALT_JOBIDs in Job Logs': unique_jobids_job_log
}

report_df = pd.DataFrame(list(verification_report.items()), columns=['Metric', 'Value'])
report_df.to_csv('C:/Users/dattu/OneDrive/Desktop/UIC_Argonne_Theta_Project/verification_report_step4.csv', index=False)
print("\nVerification report saved to 'verification_report_step4.csv'.")
