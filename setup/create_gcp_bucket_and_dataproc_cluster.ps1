# Create a storage bucket
Start-Process "gsutil" -ArgumentList "mb gs://ecom-buck2806" -NoNewWindow -Wait

# Create a Dataproc cluster
Start-Process "gcloud" -ArgumentList "dataproc clusters create ecom-cluster --region=us-central1 --zone=us-central1-a --single-node --master-machine-type=n1-standard-4 --master-boot-disk-size=500" -NoNewWindow -Wait
