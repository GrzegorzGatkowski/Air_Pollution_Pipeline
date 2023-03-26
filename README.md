# Air Pollution Hourly Data Pipeline

## Objective

This data engineering project focuses on analyzing air quality data for 100 Polish cities. The data was obtained from the Air Pollution API, which provides current, forecast, and historical air pollution data for any coordinates on the globe. The API returns data about polluting gases such as CO, NO, NO2, O3, SO2, NH3, and particulates PM2.5 and PM10.

## Architecture

![Air Pollution pipeline](https://user-images.githubusercontent.com/26925238/225983954-96b5e1e3-ef79-4a7b-aa37-840c2eee4020.jpg)

## Problem statement

The goal of this project is to determine the most polluted cities based on their Air Quality Index (AQI) levels, which have different qualitative names and correspond to different ranges of pollutant concentrations in μg/m3. The analysis is performed using historical data available from 27th November 2020 to analyze air quality trends in the cities over time.

| Qualitative name | Index | SO2 (μg/m3) | NO2 (μg/m3) | PM10 (μg/m3) | PM2.5 (μg/m3) | O3 (μg/m3) | CO (μg/m3) |
|------------------|-------|-------------|-------------|---------------|----------------|------------|-------------|
| Good             | 1     | 0-20        | 0-40        | 0-20          | 0-10           | 0-60      | 0-4400    |
| Fair             | 2     | 20-80       | 40-70       | 20-50         | 10-25          | 60-100    | 4400-9400 |
| Moderate         | 3     | 80-250      | 70-150      | 50-100        | 25-50          | 100-140   | 9400-12400|
| Poor             | 4     | 250-350     | 150-200     | 100-200       | 50-75          | 140-180   | 12400-15400|
| Very Poor        | 5     | >350        | >200        | >200          | >75            | >180      | >15400    |


## Main objective

The following steps were performed to analyze the air quality data for the 100 Polish cities:

- Data Retrieval: Air quality data was retrieved from the Air Pollution API for the 100 Polish cities.
- AQI Calculation: The AQI levels were calculated for each city based on the pollutant concentrations in the data using the AQI formula provided in the API documentation.
- City Ranking: The cities were ranked based on their AQI levels, and the most polluted cities were identified.
- Visualization: The results were visualized using Google Looker Studio.


## Dataset description

Air Pollution API provides current, forecast and historical air pollution data for any coordinates on the globe.

The API returns data about polluting gases, such as Carbon monoxide (CO), Nitrogen monoxide (NO), Nitrogen dioxide (NO2), Ozone (O3), Sulphur dioxide (SO2), Ammonia (NH3), and particulates (PM2.5 and PM10).

The dataset has the following columns:

dt: The date and time when the measurements were taken.

Carbon_Monoxide_CO: The concentration of carbon monoxide in parts per million (ppm) at the time of measurement.

Nitric_oxide_NO: The concentration of nitric oxide in parts per billion (ppb) at the time of measurement.

Nitrogen_Dioxide_NO2: The concentration of nitrogen dioxide in parts per billion (ppb) at the time of measurement.

Ozone_O3: The concentration of ozone in parts per million (ppm) at the time of measurement.

Sulfur_Dioxide_SO2: The concentration of sulfur dioxide in parts per billion (ppb) at the time of measurement.

PM2_5: The concentration of fine particulate matter with diameter less than 2.5 micrometers in micrograms per cubic meter (µg/m³) at the time of measurement.

PM10: The concentration of coarse particulate matter with diameter less than 10 micrometers in micrograms per cubic meter (µg/m³) at the time of measurement.

NH3: The concentration of ammonia in parts per billion (ppb) at the time of measurement.

City_index: An integer index representing the city where the measurements were taken.

## Proposal

### Technologies
## What technologies are being used?
- Cloud: [Google Cloud](https://cloud.google.com)
- Infrastructure: [Terraform](https://www.terraform.io/)
- Orchestration: [Prefect](https://www.prefect.io/)
- Data lake: [Google Cloud Storage](https://cloud.google.com/storage)
- Data transformation: [DBT](https://www.getdbt.com/)
- Data warehouse: [BigQuery](https://cloud.google.com/bigquery)
- Data visualization: [Google Looker Studio](https://cloud.google.com/looker)

## Dashboard example
<p align="left">
<img src="images/example_dashboard.JPG" width="600">
</p>

You can check my dashboard here:
https://lookerstudio.google.com/reporting/34c9db2f-e5e6-4fae-9a89-c89c0f134c3e
