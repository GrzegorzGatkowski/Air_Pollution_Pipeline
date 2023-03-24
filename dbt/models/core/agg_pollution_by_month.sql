{{ config(materialized='table') }}

with pollution as (
    select * from {{ ref('fact_pollution') }}
)
select 
    City,
    date_trunc(dt, month) as pollution_month,
    avg(Sulfur_Dioxide_SO2) as avg_SO2,
    avg (Nitrogen_Dioxide_NO2) as avg_NO2,
    avg (PM10) as avg_PM10,
    avg (PM2_5) as avg_PM2_5,
    avg (Ozone_O3) as avg_O3,
    avg (Carbon_Monoxide_CO) as avg_CO,
    avg (NH3) as avg_NH3,
    avg (Nitric_oxide_NO) as avg_NO
from pollution
group by 1, 2