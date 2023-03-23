from prefect.deployments import Deployment
from prefect.infrastructure.docker import DockerContainer

from prefect.server.schemas.schedules import CronSchedule
from current_parameterized_flow import etl_current_parent_flow
from history_parameterized_flow import (
    etl_cities_flow,
    etl_gcs_to_bq,
    etl_to_gcs_parent_flow,
)

docker_block = DockerContainer.load("airpollution")

hourly_dep = Deployment.build_from_flow(
    flow=etl_current_parent_flow,
    name="current-flow",
    infrastructure=docker_block,
    tags=["GCP"],
    schedule=(CronSchedule(cron="0 * * * *", timezone="America/Chicago")),
)
gcp_pollution_dep = Deployment.build_from_flow(
    flow=etl_to_gcs_parent_flow,
    name="gcp-pollution-flow",
    infrastructure=docker_block,
    tags=["GCP"],
)

gcp_to_bq_dep = Deployment.build_from_flow(
    flow=etl_gcs_to_bq,
    name="bq-pollution-flow",
    infrastructure=docker_block,
    tags=["GCP"],
)

cities_dep = Deployment.build_from_flow(
    flow=etl_cities_flow,
    name="cities-flow",
    infrastructure=docker_block,
    tags=["GCP"],
)

if __name__ == "__main__":
    hourly_dep.apply()
    gcp_pollution_dep.apply()
    gcp_to_bq_dep.apply()
    cities_dep.apply()
