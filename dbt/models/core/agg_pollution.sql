{{ config(materialized='table') }}

with pollution as (
    select * from {{ ref('fact_pollution') }}
)
select 
    City,
    count(1) as hours_count,
    pollution_quality
from pollution
group by 1, 3

    