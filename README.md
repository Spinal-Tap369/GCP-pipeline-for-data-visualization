# E-Commerce Data Pipeline

This repository contains the code to set up an end-to-end data pipeline for an e-commerce dataset using Google Cloud Platform, Hadoop, Hive, PySpark, and Looker Studio.

## Project Structure

- `setup/`: Scripts for setting up the GCP bucket and Dataproc cluster.
- `hdfs_setup/`: Commands for setting up HDFS and uploading the dataset.
- `hive_setup/`: SQL scripts for setting up Hive tables and loading data.
- `pyspark_setup/`: PySpark scripts for processing data.
- `save_dataframes/`: Scripts for saving processed data to GCS, HDFS, and Hive.
- `visualization/`: Instructions for visualizing data in Looker Studio.

## Setup Instructions

### 1. Create GCP Bucket and Dataproc Cluster
```powershell
./setup/create_gcp_bucket_and_dataproc_cluster.ps1
```
### 2. Upload Dataset to GCP Bucket
```powershell
./setup/upload_dataset_to_bucket.ps1
```

### 3. SSH into Dataproc Cluster
```powershell
./setup/ssh_into_cluster.ps1
```

### 4. HDFS Setup
```powershell
./hdfs_setup/hdfs_setup_commands.ps1
```

### 5. Hive Setup
```powershell
hive -f hive_setup/hive_setup_commands.sql
```

### 6. PySpark Setups
```powershell
pyspark pyspark_setup/pyspark_setup.py
```

### 7. Save DataFrames
```powershell
pyspark save_dataframes/save_dataframes.py
```

### 8. Visualization
Follow the instructions in `visualization/looker_studio_instructions.md.`

### Project Team Members
https://github.com/karanzaveri

https://github.com/Spinal-Tap369

https://github.com/Nick9695

https://github.com/Ulysses013
