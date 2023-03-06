from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect.tasks import task_input_hash
from datetime import datetime, timedelta
from etl_tasks import get_current_pollution, get_pollution_data, rename_columns, cleaning_columns

now = int((datetime.now() - timedelta(minutes=1)).timestamp())
week_earlier = int((datetime.now() - timedelta(days=7)).timestamp())

# Load the data
data = get_pollution_data(week_earlier, now, 49.9778328, 18.9425124)
data = cleaning_columns(data)
data = rename_columns(data)

print(data.head())

