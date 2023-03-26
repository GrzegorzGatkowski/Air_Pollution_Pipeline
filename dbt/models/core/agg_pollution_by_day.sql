{{ config(materialized='table') }}

with pollution as (
    select * from {{ ref('fact_pollution') }}
)

SELECT 
  DATE(dt) as date,
  City,
  CASE 
    WHEN COUNTIF(pollution_quality = 'Very_Poor') > 0 THEN 'Very_Poor'
    WHEN COUNTIF(pollution_quality = 'Poor') > 0 THEN 'Poor'
    WHEN COUNTIF(pollution_quality = 'Moderate') > 0 THEN 'Moderate'
    WHEN COUNTIF(pollution_quality = 'Fair') > 0 THEN 'Fair'
    WHEN COUNTIF(pollution_quality = 'Good') > 0 THEN 'Good'
    ELSE 'Unknown'
  END AS pollution_quality,
  COUNT(DISTINCT DATE(dt)) as count_days,
  avg(Sulfur_Dioxide_SO2) as avg_SO2,
    avg (Nitrogen_Dioxide_NO2) as avg_NO2,
    avg (PM10) as avg_PM10,
    avg (PM2_5) as avg_PM2_5,
    avg (Ozone_O3) as avg_O3,
    avg (Carbon_Monoxide_CO) as avg_CO,
    avg (NH3) as avg_NH3,
    avg (Nitric_oxide_NO) as avg_NO
FROM 
  pollution
WHERE 
  pollution_quality IN ('Very_Poor', 'Poor', 'Moderate', 'Fair', 'Good')
GROUP BY 
  1, 2
ORDER BY 
  date ASC




