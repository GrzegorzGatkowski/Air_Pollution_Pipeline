with pollution as (
    select *,
    row_number() over(partition by City_index, dt) as rn
    from `continual-block-378617`.`raw`.`airpollution`
    order by City_index
)
select City_index,
dt,
case 
        when Sulfur_Dioxide_SO2 > 350 OR Nitrogen_Dioxide_NO2 > 200 OR PM10 > 200 OR PM2_5 > 75 OR Ozone_O3 > 180 OR Carbon_Monoxide_CO > 15400 then 'Very_Poor'
        when Sulfur_Dioxide_SO2 > 250 OR Nitrogen_Dioxide_NO2 > 150 OR PM10 > 100 OR PM2_5 > 50 OR Ozone_O3 > 140 OR Carbon_Monoxide_CO > 12400 then 'Poor'
        when Sulfur_Dioxide_SO2 > 80 OR Nitrogen_Dioxide_NO2 > 70 OR PM10 > 50 OR PM2_5 > 25 OR Ozone_O3 > 100 OR Carbon_Monoxide_CO > 9400 then 'Moderate'
        when Sulfur_Dioxide_SO2 > 20 OR Nitrogen_Dioxide_NO2 > 40 OR PM10 > 20 OR PM2_5 > 10 OR Ozone_O3 > 60 OR Carbon_Monoxide_CO > 4400 then 'Fair'
        else 'Good'
    end as pollution_quality,
Sulfur_Dioxide_SO2,
Nitrogen_Dioxide_NO2,
PM10,
PM2_5,
Ozone_O3,
Carbon_Monoxide_CO,
NH3,
Nitric_oxide_NO
from pollution
where rn = 1

-- dbt build --m <model.sql> --var 'is_test_run: false'
