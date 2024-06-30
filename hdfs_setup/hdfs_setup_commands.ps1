# Update and install Google Cloud SDK
Start-Process "sudo" -ArgumentList "apt-get update" -NoNewWindow -Wait
Start-Process "sudo" -ArgumentList "apt-get install google-cloud-sdk" -NoNewWindow -Wait

# Authenticate with gcloud
Start-Process "gcloud" -ArgumentList "auth login" -NoNewWindow -Wait

# Copy dataset from GCS to local
Start-Process "gsutil" -ArgumentList "cp gs://ecom-buck2806/ecom-dataset.csv ." -NoNewWindow -Wait

# Create HDFS directory and upload dataset
Start-Process "hdfs" -ArgumentList "dfs -mkdir -p /user/ecom-project" -NoNewWindow -Wait
Start-Process "hdfs" -ArgumentList "dfs -put ecom-dataset.csv /user/ecom-project/" -NoNewWindow -Wait
