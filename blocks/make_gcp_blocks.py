from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

# alternative to creating GCP blocks in the UI
# copy your own service_account_info dictionary from the json file you downloaded from google
# IMPORTANT - do not store credentials in a publicly available repository!


credentials_block = GcpCredentials(
    service_account_info={}  # enter your credentials from the json file
)
credentials_block.save("airpollution-credential", overwrite=True)


bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("airpollution-credential"),
    bucket="airpollution_continual-block-378617",  # insert your  GCS bucket name
)

bucket_block.save("airpollution-gcs", overwrite=True)
