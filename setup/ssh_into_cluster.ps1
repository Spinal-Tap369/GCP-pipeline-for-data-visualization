# SSH into the cluster
Start-Process "gcloud" -ArgumentList "compute ssh ecom-cluster-m --zone=us-central1-a" -NoNewWindow -Wait
