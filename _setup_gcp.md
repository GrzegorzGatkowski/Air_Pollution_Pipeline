# GCP

## Create a GCP account

Google provides 300USD free credit available for 90 days to new accounts.

## Create a new project in GCP

When creating a project [Google Cloud Platform project](https://console.cloud.google.com/cloud-resource-manager), use a project id that is unique, edit it since it can not be modified later on. 

## Create a service account

Note: Service account authorize applications to perform authorized API calls. They are not user accounts of Google Workspace Domain  
Go to IAM -> Service accounts
- Add one service account
  - Fill the details
  - Add Viewer role (plain viewer role)
  - No need to grant access to multiple users
- Create keys in the service account
  - Actions icon -> Manage Keys -> AddKey -> Create new key -> Create
  - Save the json in a safe directory in your local computer e.g. to `~/.gc/<credentials>`


## Set up permissions to the service account for GCS y Big Query

- Go to IAM & Admin -> IAM
- Edit the service account icon -> Edit principal
- Add the following roles:
  - Storage Admin
  - Storage Object Admin
  - BigQuery Admin
  - Viewer (just 'Viewer')


## Enable IAM API for the SDK to communicate though IAM
https://console.cloud.google.com/apis/library/iam.googleapis.com

## Enable the rest of the APIs 
Be sure to have enabled the following APIs for your project in the GCP account.
- https://console.cloud.google.com/apis/library
  - Compute Engine
  - Cloud Storage
  - BigQuery  


 