

with cities as (
    select 
    City_index,
    City,
    Latitude,
    Longitude 
    from `continual-block-378617`.`development`.`stg_cities`
),

pollution as (
    select *
    from `continual-block-378617`.`development`.`stg_air_pollution`
)

select 
    City, 
    dt,
    pollution_quality,
    Sulfur_Dioxide_SO2,
    Nitrogen_Dioxide_NO2,
    PM10,
    PM2_5,
    Ozone_O3,
    Carbon_Monoxide_CO,
    NH3,
    Nitric_oxide_NO
from pollution as p
inner join cities as c
on p.City_index = c.City_index
order by City, dt