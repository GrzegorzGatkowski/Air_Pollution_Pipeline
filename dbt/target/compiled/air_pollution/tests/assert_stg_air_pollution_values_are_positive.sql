with pollution as (
    select 
    Sulfur_Dioxide_SO2, 
    Nitrogen_Dioxide_NO2, 
    PM10, 
    PM2_5, 
    Ozone_O3, 
    Carbon_Monoxide_CO, 
    NH3,
    Nitric_oxide_NO
    from `continual-block-378617`.`development`.`stg_air_pollution`
)

select *
from pollution
where Sulfur_Dioxide_SO2 < 0 
    or Nitrogen_Dioxide_NO2 < 0
    or PM10 < 0
    or PM2_5 < 0
    or Ozone_O3 < 0
    or Carbon_Monoxide_CO < 0
    or NH3 < 0
    or Nitric_oxide_NO < 0