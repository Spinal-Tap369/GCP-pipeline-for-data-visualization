# Upload dataset to GCS bucket
Start-Process "gsutil" -ArgumentList "cp ecom-dataset.csv gs://ecom-buck2806/" -NoNewWindow -Wait

